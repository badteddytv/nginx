import os
from stood.logger.logger import get_logger

service_name = os.getenv('HOSTNAME', 'UNKOWN').split('-')[0]

log = get_logger(service_name)
