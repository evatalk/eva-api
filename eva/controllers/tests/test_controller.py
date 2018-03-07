from django.test import TestCase

from core.models import MessagingService, MessagingServiceUserIdentifier, User

from ..request_controller import ModelDataVerifier, RequestDataVerifier


class ControllerTestCase(TestCase):
    def setUp(self):
        # Creating User and Messaging test models
        User.objects.create(first_name="Mauro de Carvalho",
                            messaging_service_identifier="iu124h21h2i21h")

        User.objects.create(first_name="Leonardo Minora",
                            messaging_service_identifier="fiuaha2h2hs211")

        MessagingService.objects.create(name="Telegram")

        # Getting test models
        user = User.objects.get(
            first_name="Mauro de Carvalho", messaging_service_identifier="iu124h21h2i21h")

        messaging_service = MessagingService.objects.get(name="Telegram")

        # Creating MessagingUserIdentifier test model
        MessagingServiceUserIdentifier.objects.create(
            user=user, messaging_service=messaging_service)

    def test_verifies_if_user_exists(self):
        self.assertEqual(ModelDataVerifier.verifies_if_user_exists(
            "iu124h21h2i21h"), True)

    def test_verifies_if_user_doesnt_exists(self):
        self.assertEqual(ModelDataVerifier.verifies_if_user_exists(
            "49082412902292"), False)

    def test_verifies_if_messaging_service_exists(self):
        self.assertEqual(
            ModelDataVerifier.verifies_if_messaging_service_exists("Telegram"), True)

    def test_verifies_if_messaging_service_doesnt_exists(self):
        self.assertEqual(
            ModelDataVerifier.verifies_if_messaging_service_exists("WhatsApp"), False)

    def test_verifies_if_messaging_service_user_identifier_exists(self):
        user = User.objects.get(messaging_service_identifier="iu124h21h2i21h")
        messaging_service = MessagingService.objects.get(name="Telegram")
        self.assertEqual(
            ModelDataVerifier.verifies_if_messaging_service_identifier_exists(user, messaging_service), True)

    def test_verifies_if_messaging_service_user_identifier_doesnt_exists(self):
        user = User.objects.get(messaging_service_identifier="fiuaha2h2hs211")
        messaging_service = MessagingService.objects.get(name="Telegram")
        self.assertEqual(
            ModelDataVerifier.verifies_if_messaging_service_identifier_exists(user, messaging_service), False)

    def test_verifies_if_request_body_is_valid(self):
        request_body = {
            "provider": "Telegram",
            "message": "Olá, Eva",
            "user_first_name": "Fulano",
            "provider_user_id": "289j891289ssa"}

        self.assertEqual(RequestDataVerifier.request_body_is_valid(request_body), True)
