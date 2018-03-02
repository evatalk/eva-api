from django.urls import path

from core.views import RequestHandler

urlpatterns = [
    path('message/handler', RequestHandler.as_view(), name='request_handler'),
]
