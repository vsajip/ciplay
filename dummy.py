# A dummy package for testing out CI configurations

import logging

logger = logging.getLogger(__name__)

def hello():
    logger.debug('Well, hello there.')
    return 'Hello, world!'
