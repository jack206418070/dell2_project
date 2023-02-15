# vary.py

import json
import os
from base64 import b64decode
from pathlib import Path

import openai

DATA_DIR = Path.cwd() / 'response'
SOURCE_FILE = DATA_DIR / "An ec-1675514108.json"

openai.api_key = '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'

with open(SOURCE_FILE, mode="r", encoding="utf-8") as json_file:
  saved_response = json.load(json_file)
  image_data = b64decode(saved_response["data"][0]["b64_json"])

response = openai.Image.create_variation(
  image=image_data,
  n=3,
  size="256x256"
)
print(response)

new_file_name = f"vary-{SOURCE_FILE.stem[:5]}-{response['created']}.json"

with open(DATA_DIR / new_file_name, mode="w", encoding="utf-8") as file:
  json.dump(response, file)