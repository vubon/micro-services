from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from . import views

urlpatterns = [
    url(r'^sign-up/', views.SignUpView.as_view()),
    url(r'^login-token/', obtain_jwt_token),
    url(r'^refresh-token/', refresh_jwt_token),
    url(r'^verify-token/', verify_jwt_token),
    url(r'^token-validation/', views.TokenValidation.as_view()),
    url(r'^user-validation/', views.UserValidation.as_view()),
]