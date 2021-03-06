from django.urls import path

from core.views.authentication_view import SignUp
from core.views.eva_view import EVACoreView

urlpatterns = [
    # Authentication
    path('auth/register', SignUp.as_view(), name="signup"),

    # Messages responses
    path('request', EVACoreView.as_view(), name='eva-request'),
]
