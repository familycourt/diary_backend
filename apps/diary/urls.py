from django.urls import path

from .views import DiaryCodeAPIView, DiaryCreateAPIView, DiaryRegisterAPIView


urlpatterns = [
    path('diary/', DiaryCreateAPIView.as_view()),
    path('diary/register/', DiaryRegisterAPIView.as_view()),
    path('diary/code/', DiaryCodeAPIView.as_view()),
]
