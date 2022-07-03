from django.urls import path

from .views import (DiaryCreateAPIView,
                    QuestionRetrieveAPIView,
                    AnswerListAPIView)


urlpatterns = [
    path('diary/', DiaryCreateAPIView.as_view()),
    path('question/', QuestionRetrieveAPIView.as_view()),
    path('answer/', AnswerListAPIView.as_view()),
]
