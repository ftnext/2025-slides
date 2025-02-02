import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s | %(levelname)s | %(name)s:%(funcName)s:%(lineno)d - %(message)s",
)

logger = logging.getLogger("mylib")
logger.setLevel(logging.INFO)

logger.info("想定通り")

"""
2024-08-29 21:42:01,945 | INFO | mylib:<module>:11 - 想定通り
"""
