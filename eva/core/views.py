from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from controllers.request_controller import RequestDataVerifier
from core.models import *
from eva.settings import eva_ia
from handlers.conversations.request_conversation_handler import \
    MessageFlowHandler


class EVACoreView(APIView):

    def post(self, request):
        # Verifies if the request body sent by user is valid
        if RequestDataVerifier.request_body_is_valid(dict(request.data)):
            try:
                user = User.objects.get(
                    messaging_service_identifier=request.data.get('provider_user_id'))
            except ObjectDoesNotExist:
                user = User(
                    first_name=request.data.get('user_first_name'),
                    messaging_service_identifier=request.data.get('provider_user_id'))
                user.save()

            try:
                messaging_service = MessagingService.objects.get(
                    name=request.data.get('provider'))
            except ObjectDoesNotExist:
                messaging_service = MessagingService(
                    name=request.data.get('provider'))

                messaging_service.save()

            try:
                messaging_service_identifier = MessagingServiceUserIdentifier.objects.get(
                    messaging_service=messaging_service,
                    user=user)
            except ObjectDoesNotExist:
                messaging_service_identifier = MessagingServiceUserIdentifier(
                    messaging_service=messaging_service,
                    user=user)

                messaging_service_identifier.save()

            # asks the WIT to analyze the user's intention
            wit_response_message = eva_ia.message(request.data.get('message'))

            # Get the response and the intent
            eva_text_response, intent = MessageFlowHandler.response(
                wit_response_message)

            # Creating the message
            message = Message(
                intent=intent,
                content=eva_text_response,
            )

            message.save()

            # Associating a message to a user
            user_message = UserMessage(user=user, message=message)

            user_message.save()

            message = {'response_message': eva_text_response}
            return Response(message)

        error_message = {'error': "malformed request syntax"}
        return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response(status=status.HTTP_204_NO_CONTENT)
