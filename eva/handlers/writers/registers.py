from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from core.models import UserProfile
from handlers.generators.data_generators import email_generator
from handlers.generators.numbers_generators import random_password
from handlers.readers.information_map import USER_INFORMATION_MAP


class Register(object):

    @classmethod
    def user_register(cls, user_informations):
        # User data information
        user_name = user_informations[USER_INFORMATION_MAP["nome"]]
        user_cpf = user_informations[USER_INFORMATION_MAP["cpf"]]

        
        # Checks if the user has an email in the database,
        # otherwise we will generate one for him.
        # *** User is a required field in the Django User model
        if user_informations[USER_INFORMATION_MAP["login_liferay"]]:
            user_email = user_informations[USER_INFORMATION_MAP["login_liferay"]]
        else:
            user_email = email_generator(user_cpf)

        # Checks if user is already registered
        if cls._check_if_user_already_exists(user_email, user_cpf):
            return cls._returns_user_token(user_email)

        # generates a random password
        password = random_password()

        # Creating a User instance
        user = User.objects.create_user(
            user_email, user_email, password)

        # Saves the user in the database
        user.save()

        # Creating a UserProfile instance
        user_profile = UserProfile(
            name=user_name,
            cpf=user_cpf,
            user=user,
        )

        # Saves in the database
        user_profile.save()

        return cls._returns_user_token(user.email)

    @classmethod
    def _check_if_user_already_exists(cls, email, cpf):
        return User.objects.filter(email=email).exists() or UserProfile.objects.filter(cpf=cpf).exists()

    @classmethod
    def _returns_user_token(cls, user_email):
        user = User.objects.get(email=user_email)
        token, created = Token.objects.get_or_create(user=user)

        return token.key
