from django.test import TestCase
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase


class EVATests(APITestCase):

    def setUp(self):
        factory = APIRequestFactory()

    def test_get(self):
        pass
