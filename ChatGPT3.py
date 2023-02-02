import logging
import os
import openai


class ChatGPT3(object):
    """
    The aim of ChatGPT3 is to imitate ChatGPT's functionality with GPT-3 API, though conversations must be brief due
    to the 4000 token constraint for Text-Davinci-003.
    Author Credits: OpenAI
    """
    def __init__(self, config=None):
        if config is None:
            config = {"model": "text-davinci-003",
                      "context": ""}
        self.openai_api_key = os.environ.get('OPENAI_API_KEY')
        self.model = config['model']
        self.context = config['context']

    def get_response(self, text):
        openai.api_key = self.openai_api_key
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=text,
            temperature=0.7,
            max_tokens=4000,
            top_p=0.9,
            frequency_penalty=1,
            presence_penalty=0
        )
        return response['choices'][0]['text']

    def chat(self, text):
        response = self.get_response(self.context + text)
        self.context += text + "\n"
        logging.info(response)
        return response
