import logging
from unittest import TestCase

from JochemChat import JochemChat

logging.basicConfig(level=logging.INFO)


class TestJochemChat(TestCase):
    """
    Author: stan.chen@plusgpt.app
    """
    def test_get_response(self):
        config = {"model": "text-davinci-003",
                  "context": ""}
        convo = JochemChat(config=config)
        data = convo.get_response("What are 10 frontend frameworks?")
        logging.info(data)
        assert data is not None

    def test_chat(self):
        config = {"model": "text-davinci-003",
                  "context": ""}
        convo = JochemChat(config=config)
        data = convo.chat("What are 10 frontend frameworks?")
        logging.info(data)
        data = convo.chat("which of the frameworks are best for beginners?")
        logging.info(data)
        assert data is not None
