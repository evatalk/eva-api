from random import choice

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from controllers.request_controller import UserRequestInformation
from eva.settings import INFORMATIONS_STORAGE_PATH
from handlers.readers.information_readers import StorageInformationReader
from handlers.writers.eva_responses import EvaResponseWriter


class EvaController(object):

    def __init__(self, intent, request):
        self.intent = intent
        self.request = request

    def response(self):
        """check with what intent the user should be answered."""
        return self.intent_map()

    def intent_map(self):
        """map of intentions.

        Here it will be decided which response will
        be chosen from the intention of the user's
        message.
        """

        if self.intent == "greetings":
            return self.returns_a_greetings_response()

        elif self.intent == "cursing":
            return self.returns_a_non_cursing_response()

        elif self.intent == "history":
            return self.returns_the_user_courses_history()

        elif self.intent == "certificate":
            return self.returns_the_finished_courses()
        
        elif self.intent == "open_to_subscription":
            return self.returns_courses_open_to_subscription()

        else:
            return self.returns_a_default_response("default")

    def returns_the_user_courses_history(self):
        """Courses history.

        Displays all courses that the user is enrolled
        in or has already completed.        
        """
        data_reader = StorageInformationReader(INFORMATIONS_STORAGE_PATH)
        user_cpf = UserRequestInformation.get_user_cpf(self.request)
        users_courses_data = data_reader.user_courses_history(user_cpf)
        intent = self.get_intent()
        status_code = status.HTTP_200_OK

        return Response({"intent": intent, "content": users_courses_data}, status=status_code)

    def returns_a_greetings_response(self):
        """Greetings message.

        Randomly returns one of the greetings messages
        to the user.
        """
        intent = self.get_intent()
        status_code = status.HTTP_200_OK

        return Response({"intent": intent}, status=status_code)

    def returns_a_non_cursing_response(self):
        """Cursing response.

        Randomly returns one of the curses response messages.
        """
        intent = self.get_intent()
        status_code = status.HTTP_200_OK

        return Response({"intent": intent}, status=status_code)

    def returns_the_finished_courses(self):
        """Courses that can be certified.

        Returns all courses in which the user can issue the
        certification.
        """
        data_reader = StorageInformationReader(INFORMATIONS_STORAGE_PATH)
        user_cpf = UserRequestInformation.get_user_cpf(self.request)
        intent = self.get_intent()
        
        user_courses_history_information = data_reader.user_courses_history_to_analyze(
            user_cpf=user_cpf, user_enrollement=None)

        eva_response_writer = EvaResponseWriter(
            user_courses_history_information)
        intent = self.get_intent()
        status_code = status.HTTP_200_OK

        return Response({"intent": intent, "content": eva_response_writer.finished_courses_response()}, status=status_code)

    def returns_a_default_response(self, intent):
        """Default response.

        if the intention is not detected, one of the default
        response messages will be chosen randomly.
        """
        #intent = self.get_intent()
        status_code = status.HTTP_200_OK

        return Response({"intent": intent}, status=status_code)

    def returns_courses_open_to_subscription(self):
        data_reader = StorageInformationReader(INFORMATIONS_STORAGE_PATH)
        user_cpf = UserRequestInformation.get_user_cpf(self.request)
        open_for_subscription_data = data_reader.courses_open_for_subscriptions(user_cpf)
        intent = self.get_intent()
        status_code = status.HTTP_200_OK

        return Response({"intent": intent, "content": open_for_subscription_data}, status=status_code)

    def get_intent(self):
        """Returns the intention."""
        return self.intent
