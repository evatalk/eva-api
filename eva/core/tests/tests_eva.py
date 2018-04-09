from django.test import TestCase
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase


class EVATests(APITestCase):

    def setUp(self):
        factory = APIRequestFactory()

    def test_get(self):
        url = reverse('eva-request')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
