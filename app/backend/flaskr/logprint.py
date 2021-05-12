import os
import logging

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')

'''
Setup logger format, level, and handler.

RETURNS: log object
'''
def _logger(__name__):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    log = logging.getLogger(__name__)
    log.setLevel(LOG_LEVEL)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    log.addHandler(stream_handler)
    return log
