import aioredis
import asyncio
from logger import log
from config import config


async def redis_pool():
    while True:
        try:
            redis = await aioredis.create_redis_pool(config.REDIS_URL)
            break
        except Exception:
            log.exception('error connecting to redis, retrying in 5s')
            await asyncio.sleep(5)
    return redis

redis = asyncio.get_event_loop().run_until_complete(redis_pool())
