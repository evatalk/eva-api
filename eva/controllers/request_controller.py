from django.core.exceptions import ObjectDoesNotExist

from core.models import (Message, MessagingService,
                         MessagingServiceUserIdentifier, User, UserMessage)


class ModelDataVerifier(object):

    @classmethod
    def verifies_if_messaging_service_exists(cls, messaging_service_name):
        exists = True
        try:
            messaging_service = MessagingService.objects.get(
                name=messaging_service_name)
        except ObjectDoesNotExist:
            exists = False

        return exists

    @classmethod
    def verifies_if_user_exists(cls, user_messaging_service_identifier):
        exists = True
        try:
            user = User.objects.get(
                messaging_service_identifier=user_messaging_service_identifier)
        except ObjectDoesNotExist:
            exists = False

        return exists

    @classmethod
    def verifies_if_messaging_service_identifier_exists(cls, user, messaging_service):
        exists = True
        try:
            messaging_service_identifier = MessagingServiceUserIdentifier.objects.get(
                user=user, messaging_service=messaging_service)
        except ObjectDoesNotExist:
            exists = False

        return exists


class RequestDataVerifier(object):
    @classmethod
    def _verifies_if_provider_is_not_null(cls, request_body):
        try:
            provider = request_body['provider']
        except KeyError:
            return False

        return provider is not None

    @classmethod
    def _verifies_if_message_is_not_null(cls, request_body):
        try:
            message = request_body['message']
        except KeyError:
            return False

        return message is not None

    @classmethod
    def _verifies_if_user_first_name_is_not_null(cls, request_body):
        try:
            user_first_name = request_body['user_first_name']
        except KeyError:
            return False

        return user_first_name is not None

    @classmethod
    def _verifies_if_provider_user_id_is_not_null(cls, request_body):
        try:
            provider_user_id = request_body['provider_user_id']
        except KeyError:
            return False

        return provider_user_id is not None

    @classmethod
    def request_body_is_valid(cls, request_body):
        return (
            cls._verifies_if_message_is_not_null(request_body)
            and cls._verifies_if_provider_is_not_null(request_body)
            and cls._verifies_if_provider_user_id_is_not_null(request_body)
            and cls._verifies_if_user_first_name_is_not_null(request_body))
