from random import choice

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from controllers.request_controller import UserRequestInformation
from eva.settings import INFORMATIONS_STORAGE_PATH
from handlers.conversations.responses import RESPONSE_MAP
from handlers.readers.information_readers import StorageInformationReader
from handlers.writers.eva_responses import EvaResponseWriter


class EvaController(object):

    def __init__(self, intent, request):
        self.intent = intent
        self.request = request

    def response(self):
        return self.intent_map()

    def intent_map(self):
        if self.intent == "greetings":
            return self.returns_a_greetings_response()

        elif self.intent == "cursing":
            return self.returns_a_non_cursing_response()

        elif self.intent == "history":
            return self.returns_the_user_courses_history()

        elif self.intent == "certificate":
            return self.returns_the_finished_courses()

        else:
            return self.returns_a_default_response("default")

    def returns_the_user_courses_history(self):
        data_reader = StorageInformationReader(INFORMATIONS_STORAGE_PATH)

        user_cpf = UserRequestInformation.get_user_cpf(self.request)

        users_courses_data = data_reader.user_courses_history(user_cpf)

        status_code = status.HTTP_200_OK

        return Response({"content": users_courses_data}, status=status_code)

    def returns_a_greetings_response(self):
        greetings_message = choice(RESPONSE_MAP[self.intent])
        status_code = status.HTTP_200_OK

        return Response({"message": greetings_message}, status=status_code)

    def returns_a_non_cursing_response(self):
        non_cursing_message = choice(RESPONSE_MAP[self.intent])
        status_code = status.HTTP_200_OK

        return Response({"message": non_cursing_message}, status=status_code)

    def returns_the_finished_courses(self):
        data_reader = StorageInformationReader(INFORMATIONS_STORAGE_PATH)
        user_cpf = UserRequestInformation.get_user_cpf(self.request)

        user_courses_history_information = data_reader.user_courses_history_to_analyze(
            user_cpf=user_cpf, user_enrollement=None)

        eva_response_writer = EvaResponseWriter(
            user_courses_history_information)

        status_code = status.HTTP_200_OK

        return Response({"message": eva_response_writer.finished_courses_response()}, status=status_code)

    def returns_a_default_response(self, intent):
        default_message = choice(RESPONSE_MAP[intent])
        status_code = status.HTTP_200_OK

        return Response({"message": default_message}, status=status_code)
