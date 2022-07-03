from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import SignUpAPIView

urlpatterns = [
    path('auth/signin/', TokenObtainPairView.as_view()),
    path('auth/signup/', SignUpAPIView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
]
