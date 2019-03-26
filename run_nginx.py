import asyncio
import time
import subprocess
import aioredis
from config import config
from logger import log


async def redis_pool():
    while True:
        try:
            redis = await aioredis.create_redis_pool(config.REDIS_URL)
            break
        except Exception:
            log.warning('error connecting to redis, retrying in 5s')
            await asyncio.sleep(5)
    return redis

redis = asyncio.get_event_loop().run_until_complete(redis_pool())

subprocess.Popen([
            '/usr/local/nginx/sbin/nginx',
            '-g',
            '"daemon off;"'],
            shell=True
            )


host_set = set()


async def run_reload_loop():
    global host_set
    while True:
        current_set = set()
        cur = b'0'  # set initial cursor to 0
        while cur:
            cur, keys = await redis.scan(cur)
            for k in keys:
                current_set.add(k)
        if host_set != current_set:
            log.info('reloading')
            subprocess.Popen('/usr/local/nginx/sbin/nginx -s reload', shell=True)

        host_set = current_set
        await asyncio.sleep(5)

asyncio.get_event_loop().run_until_complete(run_reload_loop())
