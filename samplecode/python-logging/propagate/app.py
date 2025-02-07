import logging

from mylib import example

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s | %(levelname)s | %(name)s:%(funcName)s:%(lineno)d - %(message)s",
)

logger = logging.getLogger("mylib")
logger.setLevel(logging.INFO)

example()

"""
2025-02-07 12:16:19,804 | INFO | mylib:example:7 - 想定通り
"""
