from random import choice

from .responses import response_map


class MessageFlowHandler(object):

    @classmethod
    def response(cls, request):
        intent = cls._get_intent(request)

        return cls._choose_intent_response(intent)

    @classmethod
    def _get_intent(cls, wit_response):
        try:
            # Que feio!
            intent = wit_response['entities']['intent'][0]['value']
        except KeyError:
            intent = "connection_problems"

        return intent

    @classmethod
    def _choose_intent_response(cls, intent):
        return choice(response_map[intent])
