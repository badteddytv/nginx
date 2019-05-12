import os


class Config(object):
    REDIS_URL = "redis://redis-containers:6389"
    DISABLE_RELOAD = os.getenv('STOOD_DISABLE_RELOAD', False)


config = Config()
