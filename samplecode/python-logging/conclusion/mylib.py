import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def awesome():
    logger.info("想定通り")
    logger.warning("ちょっとヤバいよ")
