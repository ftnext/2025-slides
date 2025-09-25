# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "httpx",
#     "rich",
#     "structlog",
# ]
# ///
import datetime
import logging

import httpx
import structlog
from rich.pretty import pprint


def add_millisecond_timestamp(logger, name, event_dict):
    dt = datetime.datetime.now()
    event_dict["timestamp"] = f"{dt:%Y-%m-%d %H:%M:%S},{dt.microsecond // 1000:03d}"
    return event_dict


shared_processors = [
    structlog.stdlib.add_logger_name,
    structlog.stdlib.add_log_level,
    structlog.stdlib.PositionalArgumentsFormatter(),
    add_millisecond_timestamp,  # TimeStamper(fmt="iso")よりもstdlib loggingに寄せる
    structlog.processors.StackInfoRenderer(),
    structlog.processors.format_exc_info,
    structlog.processors.UnicodeDecoder(),
    structlog.processors.CallsiteParameterAdder(
        {
            structlog.processors.CallsiteParameter.FILENAME,
            structlog.processors.CallsiteParameter.FUNC_NAME,
            structlog.processors.CallsiteParameter.LINENO,
        }
    ),
]

structlog.configure(
    processors=shared_processors
    + [
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

formatter = structlog.stdlib.ProcessorFormatter(
    foreign_pre_chain=shared_processors,
    processors=[
        structlog.stdlib.ProcessorFormatter.remove_processors_meta,
        structlog.dev.ConsoleRenderer(),
    ],
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)
root_logger = logging.getLogger()
root_logger.addHandler(handler)
root_logger.setLevel(logging.DEBUG)
handler.addFilter(logging.Filter("httpx"))

resp = httpx.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
