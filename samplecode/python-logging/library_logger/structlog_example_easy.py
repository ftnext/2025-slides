# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "httpx",
#     "rich",
#     "structlog",
# ]
# ///
import logging

import httpx
import structlog
from rich.pretty import pprint

structlog.stdlib.recreate_defaults(log_level=logging.DEBUG)

root_handler = logging.getLogger().handlers[0]
root_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s | %(levelname)s (%(name)s) | %(filename)s:%(funcName)s:%(lineno)d - %(message)s"
    )
)
root_handler.addFilter(logging.Filter("httpx"))

resp = httpx.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
