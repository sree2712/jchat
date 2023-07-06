import logging
import json
import re
import openai


class JochemChat(object):
    """
    The aim of ChatGPT3 is to imitate ChatGPT's functionality with GPT-3 API, though conversations must be brief due
    to the 4000 token constraint for Text-Davinci-003.
    Author Credits: OpenAI
    """
    def __init__(self, config=None):
        if config is None:
            config = {"model": "text-davinci-003",
                      "context": ""}
        self.openai_api_key = "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"
        self.model = config['model']
        self.context = config['context']

    def get_response(self, text):
        openai.api_key = self.openai_api_key
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=text,
                temperature=0.7,
                max_tokens=2500,
                top_p=0.9,
                frequency_penalty=1,
                presence_penalty=0
            )
            return response['choices'][0]['text']
        except openai.error.InvalidRequestError as e:
            if "maximum context length is" in str(e):
                error_msg = "InvalidRequestError: The maximum context length is exceeded."
            else:
                error_msg = "InvalidRequestError: {}".format(str(e))
            logging.error("InvalidRequestError: {}".format(str(e)))
            return error_msg
        

    def chat(self, text):
        response = self.get_response(self.context + text)
        self.context += text + "\n"
        logging.info(response)
        return response
    
    # get search keyword queries from GPT
    def get_keywords_gpt(self, user_question):
        
        # Access the data from the JSON file
        with open('prompt_template_kw.json', 'r') as file:
            prompt_template = json.load(file)
        # Access the data from the JSON file
        prefix = prompt_template['prefix']
        examples = prompt_template['examples']
        suffix = prompt_template['suffix']

        prompt = prefix + examples + suffix + user_question
        #actual call to GPT comes here, but until then
        response = self.get_response(self.context + prompt)
        matches_kb = re.findall(r"Search\[(.*?)\]", response)
        matches_gpt = re.findall(r"SearchPrevious\[(.*?)\]", response)
        dict_match = {}
        if not matches_kb or not matches_gpt:
            result = response
        else:
            dict_match['kb'] = matches_kb
            dict_match['gpt'] = matches_gpt
            result = dict_match
        logging.info(self.context)
        return result
    
    # route the API call for knowledge 
    def get_knowledge_gpt(keywords):
        # call to self.chat
        return ""
    
    def get_summary_from_gpt(user_question, knowledge):
        return ""