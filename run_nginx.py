import asyncio
import time
import subprocess
import aioredis
from config import config


async def redis_pool():
    while True:
        try:
            redis = await aioredis.create_redis_pool(config.REDIS_URL)
            break
        except Exception:
            await asyncio.sleep(5)
    return redis

redis = asyncio.get_event_loop().run_until_complete(redis_pool())

subprocess.Popen([
            '/usr/local/nginx/sbin/nginx',
            '-g',
            '"daemon off;"'],
            shell=True
            )

while True:
    #print('reloading')
    #subprocess.Popen([
    #        '/usr/local/nginx/sbin/nginx',
    #        '-s',
    #        'reload',
    #        '-g',
    #        '"daemon off;"'
    #        ],
    #        shell=True)
    time.sleep(3)
