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

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s (%(name)s) | %(filename)s:%(funcName)s:%(lineno)d - %(message)s",
)
logging.getLogger().handlers[0].addFilter(logging.Filter("httpx"))

resp = httpx.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
