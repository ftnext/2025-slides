# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "httpx",
#     "PyYAML",
#     "rich",
# ]
# ///
import logging.config
from pathlib import Path

import httpx
import yaml
from rich.pretty import pprint

config_path = Path(__file__).parent / "config.yml"
with config_path.open() as f:
    config = yaml.safe_load(f)
logging.config.dictConfig(config)

resp = httpx.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
