from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class RequestHandler(APIView):
    
    def post(self, request):
        return Response(status=status.HTTP_204_NO_CONTENT)