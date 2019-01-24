from django.urls import path
from .views import APIGatewayPostMethod

urlpatterns = [
    path('', APIGatewayPostMethod.as_view()),
]
