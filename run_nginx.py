import asyncio
import time
from logger import log
from render import render_and_save
from nginx import start, reload_config
from redis import redis


def parse_keys(keys):
    data = {}
    for k in keys:
        data_array = k.split('_')

        if data_array[0] != 'healthy':
            continue
        try:
            name = data_array[1]
            host = data_array[2]
            port = data_array[3]
        except IndexError:
            continue

        if name not in data:
            data[name] = []

        data[name].append({'host': host, 'port': port})

    return data


host_set = set()

# give nginx some time to start up before reloading


async def run_reload_loop():
    global host_set
    while True:
        current_set = set()
        cur = b'0'  # set initial cursor to 0
        while cur:
            cur, keys = await redis.scan(cur)
            for k in keys:
                current_set.add(k.decode('utf-8'))

        if host_set != current_set:
            data = parse_keys(current_set)
            log.info('reloading')
            reload_config()
            render_and_save(data)
        host_set = current_set
        print(host_set)
        await asyncio.sleep(5)

start()
time.sleep(3)
asyncio.get_event_loop().run_until_complete(run_reload_loop())
