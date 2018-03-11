from django.urls import path

from core.views.eva_view import EVACoreView

urlpatterns = [
    path('message/handler', EVACoreView.as_view(), name='request_handler'),
]
