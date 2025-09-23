# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "httpx",
#     "rich",
# ]
# ///
import logging
import logging.handlers

import httpx
from rich.pretty import pprint

detailed_formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s (%(name)s) | %(filename)s:%(funcName)s:%(lineno)d - %(message)s"
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(detailed_formatter)

rotate_handler = logging.handlers.TimedRotatingFileHandler(
    "app.log", when="D", backupCount=7, encoding="utf-8"
)
rotate_handler.setLevel(logging.DEBUG)
rotate_handler.setFormatter(detailed_formatter)

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(console_handler)
root_logger.addHandler(rotate_handler)

resp = httpx.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
