from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .conversations.request_handler import MessageFlowHandler
from eva.settings import eva_ia


class RequestHandler(APIView):

    def post(self, request):
        wit_response_message = eva_ia.message(request.data.get('message'))
        eva_response = MessageFlowHandler.response(wit_response_message)

        message = {'response_message': eva_response}
        return Response(message)

    def get(self, request):
        return Response(status=status.HTTP_204_NO_CONTENT)
