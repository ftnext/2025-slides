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

structlog.configure(
    processors=[
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
)

formatter = structlog.stdlib.ProcessorFormatter(
    processors=[structlog.dev.ConsoleRenderer()]
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)
root_logger = logging.getLogger()
root_logger.addHandler(handler)
root_logger.setLevel(logging.DEBUG)

resp = httpx.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
