from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import *

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('success_registration/', SuccessfulRegistrationView.as_view(), name='successful-registration'),
    path('activation/', ActivationView.as_view(), name='activation'),
    path('login/', SingInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('change_password/', ChangePassword.as_view(), name='change-password'),
    # path('forgot_password/', ForgotPasswordView.as_view(), name='forgot-password'),
]