from random import choice
from controllers.eva_functions import EvaController


class MessageFlowHandler(object):

    @classmethod
    def get_response(cls, request, wit_response):
        intent = cls._get_intent(wit_response)

        return cls._choose_intent_response(request, intent)

    @classmethod
    def _get_intent(cls, wit_response):
        try:
            # Que feio!
            intent = wit_response['entities']['intent'][0]['value']
        except KeyError:
            intent = "default"

        return intent

    @classmethod
    def _choose_intent_response(cls, request, intent):
        eva_response_controller = EvaController(intent, request)

        return eva_response_controller.response()
