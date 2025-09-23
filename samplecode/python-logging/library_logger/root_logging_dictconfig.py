# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "httpx",
#     "rich",
# ]
# ///
import logging.config

import httpx
from rich.pretty import pprint

logging.config.dictConfig(
    {
        "version": 1,
        "loggers": {
            "httpx": {
                "level": "DEBUG",
                "handlers": ["console"],
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "detailed",
            },
        },
        "formatters": {
            "detailed": {
                "format": "%(asctime)s | %(levelname)s (%(name)s) | %(filename)s:%(funcName)s:%(lineno)d - %(message)s"
            },
        },
    }
)

resp = httpx.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
