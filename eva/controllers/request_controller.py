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
