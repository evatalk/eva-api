from django.urls import path

from core.views import EVACoreView

urlpatterns = [
    path('message/handler', EVACoreView.as_view(), name='request_handler'),
]
