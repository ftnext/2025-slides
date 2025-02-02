import logging

logger = logging.getLogger("mylib")
logger.addHandler(logging.NullHandler())


def awesome():
    logger.info("想定通り")
