from django.test import TestCase

from ..conversations.request_conversation_handler import MessageFlowHandler
from ..conversations.responses import response_map


class ConversationTestCase(TestCase):

    def test_response_intent_greetings(self):
        wit_response_json_greetings = {
            "_text": "oi, eva",
            "entities": {
                "intent": [{
                    "confidence": 0.99204789628122,
                    "value": "greetings"}]},
            "msg_id": "0gmiTaHqMxhaXbBJD"}

        message, intent = MessageFlowHandler.response(
            wit_response_json_greetings)

        self.assertEqual(intent, 'greetings')
        self.assertEqual(message in response_map['greetings'], True)

    def test_response_intent_cursing(self):
        wit_response_json_cursing = {
            "_text": "vsf, eva",
            "entities": {
                "intent": [{
                    "confidence": 0.97325235494532,
                    "value": "cursing"}]},
            "msg_id": "0F4HAL8HCcFiKXz0o"}

        message, intent = MessageFlowHandler.response(
            wit_response_json_cursing)

        self.assertEqual(intent, 'cursing')
        self.assertEqual(message in response_map['cursing'], True)

    def test_response_intent_how_are_you(self):
        wit_response_json_how_are_you = {
            "_text": "tudo bem?",
            "entities": {
                "intent": [{
                    "confidence": 0.99287811294517,
                    "value": "how_are_you"}]},
            "msg_id": "0mEc95B3c0yvvp5D1"}

        message, intent = MessageFlowHandler.response(
            wit_response_json_how_are_you)

        self.assertEqual(intent, 'how_are_you')
        self.assertEqual(message in response_map['how_are_you'], True)


    def test_response_intent_not_recognized(self):
        wit_response_json_problem = {
            "_text": "n\u00e3o",
            "entities": {},
            "msg_id": "0uvCe0Tkgf9PLlsSO"}

        message, intent = MessageFlowHandler.response(
            wit_response_json_problem)

        self.assertEqual(intent, 'connection_problems')
        self.assertEqual(message in response_map['connection_problems'], True)
