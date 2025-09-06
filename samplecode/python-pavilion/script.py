# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "openai",
# ]
# ///

# https://platform.openai.com/docs/quickstart?api-mode=responses
import argparse

from openai import OpenAI

parser = argparse.ArgumentParser()
parser.add_argument("input")
args = parser.parse_args()

client = OpenAI()
response = client.responses.create(model="gpt-5", input=args.input)
print(response.output_text)
