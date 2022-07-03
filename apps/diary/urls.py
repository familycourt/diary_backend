from django.urls import path

from .views import DiaryCreateAPIView


urlpatterns = [
    path('diary/', DiaryCreateAPIView.as_view()),
]
