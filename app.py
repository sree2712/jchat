import logging
from flask import Flask, request, jsonify
import requests
from JochemChat import JochemChat


def your_function(data):
    # Your code here
    # Process the data and perform necessary operations

    # Return the result
    return {'user asked': data["user question"]}


app = Flask(__name__)

app.logger.setLevel(logging.INFO)

@app.route('/api/talktojochem', methods=['POST'])
def talk_to_jochem():
    # Get the data sent with the API request
    data = request.json

    # Initialize the GPT instance
    config = {"model": "text-davinci-003",
                    "context": ""}
    chatwithgpt = JochemChat(config=config)

    # Call to GPT
    response = chatwithgpt.chat(data["user question"])

    # Return the result as a JSON response
    return jsonify(response)

# placeholder for staging API call -> get_knowledge_kb
@app.route('/api/joke')
def get_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    headers = {'User-Agent': 'Your App Name'}  # Optional headers

    response = requests.get(url, headers=headers)
    data = response.json()

    return jsonify(data["value"])

@app.route('/api/talktowisejochem', methods=['POST'])
def talk_to_wise_jochem():

    data = request.json
    # Initialize the GPT instance
    config = {"model": "text-davinci-003",
                    "context": ""}
    chatwithgpt = JochemChat(config=config)

    # Call to GPT for keywords, returns a a dictionary
    response = chatwithgpt.get_keywords_gpt(data["user question"])

    # if matches_gpt not empty then call get_knowledge_gpt

    # if matches_kb not empty then call get_knowledge_kb

    # do some combination of knowledge append with original question and call chatwithgpt.get_summary_from_gpt

    # Return the result as a JSON response
    return jsonify(response)

