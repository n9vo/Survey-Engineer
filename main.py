from flask import Flask, redirect, render_template, request
from openai import OpenAI
import json, os


app = Flask(__name__)


client = OpenAI(api_key="")

_format = open("format.json", "r").read()


async def generate(prompt, engineer):
  response = client.chat.completions.create(model="gpt-3.5-turbo",
                                            messages=[{
                                                "role": "system",
                                                "content": engineer
                                            }, {
                                                "role": "user",
                                                "content": prompt
                                            }])

  name = json.loads(response.choices[0].message.content)['survey_name']

  data = str(json.loads(response.choices[0].message.content))

  json_chars = ['{', '}', ",", " ", ":", '[', ']']
  bad_indexes = []

  i = 0
  for char in (data):
    if char == "'":
      if not (data)[i - 1] in json_chars and not (data)[i + 1] in json_chars:
        bad_indexes.append(i)

    i = i + 1

  data_arr = []

  for char in data:
    data_arr.append(char)

  for index in bad_indexes:
    data_arr[index] = ""

  data = ""
  for char in data_arr:
    data += char

  return (data.replace("'", '"'))


@app.route('/')
def main():
  return render_template("index.html", **locals())


@app.route('/submit', methods=['POST'])
async def submit():
  prompt = request.form['prompt']

  data = await generate(
      prompt,
      'You are an assistant capable of taking a users description of a survey, and turning it into json data (NEVER USE APOSTROPHES/SINGLE QUOTES IN THE JSON). You should ONLY output json data, with this format: '
      + _format)

  return render_template("json.html", JSON=data)


@app.route('/update', methods=['POST'])
async def update():
  json = request.form['json']
  prompt = request.form['prompt']

  data = await generate(
      prompt,
      'Your job is to modify the following json according to the user input, but ONLY do what the user tells you to. If you are not told to remove something, dont remove it. Only change, add, or remove, what the user tells you to: '
      + json +
      " And this is the format of how the surveys are constructed: " +
      _format)

  return render_template("json.html", JSON=data)


app.run("0.0.0.0", 80)
