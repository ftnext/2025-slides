# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "httpx",
#     "loguru",
#     "rich",
# ]
# ///
import inspect
import logging

import httpx
from loguru import logger
from rich.pretty import pprint


# https://github.com/Delgan/loguru#entirely-compatible-with-standard-logging
class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        try:
            level: str | int = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = inspect.currentframe(), 0
        while frame:
            filename = frame.f_code.co_filename
            is_logging = filename == logging.__file__
            is_frozen = "importlib" in filename and "_bootstrap" in filename
            if depth > 0 and not (is_logging or is_frozen):
                break
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


# logging.basicConfig(handlers=[InterceptHandler()], level=logging.DEBUG)
# logging.getLogger().handlers[0].addFilter(logging.Filter("httpx"))
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
intercept_handler = InterceptHandler()
root_logger.addHandler(intercept_handler)
intercept_handler.addFilter(logging.Filter("httpx"))

resp = httpx.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
