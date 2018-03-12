from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from eva.settings import eva_ia
from handlers.conversations.request_conversation_handler import \
    MessageFlowHandler


class EVACoreView(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        # asks the WIT to analyze the user's intention
        wit_response_message = eva_ia.message(request.data.get('message'))

        # Get the response and the intent
        eva_response = MessageFlowHandler.get_response(
            request, wit_response_message)

        return eva_response

    def get(self, request):
        return Response(status=status.HTTP_204_NO_CONTENT)
