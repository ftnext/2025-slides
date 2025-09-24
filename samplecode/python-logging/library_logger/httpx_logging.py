# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "httpx",
#     "rich",
# ]
# ///
import logging

import httpx
from rich.pretty import pprint

httpx_logger = logging.getLogger("httpx")
httpx_logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
detailed_formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s (%(name)s) | %(filename)s:%(funcName)s:%(lineno)d - %(message)s"
)
console_handler.setFormatter(detailed_formatter)
httpx_logger.addHandler(console_handler)

resp = httpx.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
