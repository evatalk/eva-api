from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from eva.settings import INFORMATIONS_STORAGE_PATH
from handlers.readers.information_readers import StorageInformationReader
from handlers.writers.registers import Register


class SignUp(APIView):
    def post(self, request):
        data_reader = StorageInformationReader(INFORMATIONS_STORAGE_PATH)

        # Request data
        informed_cpf = request.data.get("cpf")
        informed_email = request.data.get("email")

        is_valid, user_information = data_reader.check_the_information_veracity(
            informed_cpf, informed_email)

        if is_valid:
            register_token = Register.user_register(user_information)
            return Response({"token": register_token}, status=status.HTTP_201_CREATED)

        return Response({"response": "Os dados informados não conferem."}, status=status.HTTP_401_UNAUTHORIZED)
