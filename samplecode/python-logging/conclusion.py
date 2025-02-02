import logging

logger = logging.getLogger("mylib")
logger.addHandler(logging.NullHandler())

logger.info("想定通り")
logger.warning("ちょっとヤバいよ")
