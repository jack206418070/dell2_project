# import os
import openai
# import json
# from base64 import b64decode
# from pathlib import Path
from flask import Flask, render_template, make_response, redirect, url_for, session, flash, jsonify, send_from_directory, request
from flask_cors import CORS
import os


app = Flask(
  __name__,
  static_folder='public',
  static_url_path='/'
)
CORS(app)
openai.api_key = os.getenv("OPENAI_API_KEY") # your api key
openai.Model.list()

def gptImage(prompt):
  print(prompt)
  # DATA_DIR = Path.cwd() / 'response'
  # DATA_DIR.mkdir(exist_ok=True)
  # PROMPT = prompt

  # print(data)
  res = openai.Image.create(
    prompt=prompt,
    n=2,
    size="256x256",
    # response_format="b64_json"
  )
  # file_name = DATA_DIR / f"{PROMPT[:5]}-{res['created']}.json"
  # with open(file_name, mode="w", encoding="utf-8") as file:
  # json.dump(res, file)
  return res['data']

# def chatAI():
#   res = openai.Completion.create(
#     model="text-davinci-003",
#     prompt='嗨!',
#     temperature=1,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0.6
#   )
#   print(res['choices'][0]['text'].strip())
# chatAI()

@app.route('/api/getImage')
def getImage():
  prompt = request.args.get('prompt')
  res = gptImage(prompt)
  return jsonify(res)

# @app.route('/')
# def index():
#   return render_template('index_0216.html')

@app.route('/')
def dell():
  return render_template('index.html')

if __name__ == "__main__":
  app.run()