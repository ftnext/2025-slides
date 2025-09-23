# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "httpx",
#     "python-json-logger",
#     "rich",
# ]
# ///
import logging

import httpx
from pythonjsonlogger.json import JsonFormatter
from rich.pretty import pprint

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
json_formatter = JsonFormatter(
    "%(asctime)s | %(levelname)s (%(name)s) | %(filename)s:%(funcName)s:%(lineno)d - %(message)s"
)
console_handler.setFormatter(json_formatter)
root_logger.addHandler(console_handler)
console_handler.addFilter(logging.Filter("httpx"))

resp = httpx.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
