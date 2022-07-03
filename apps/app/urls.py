from django.urls import path

from .views import (AnswerAPIView, DiaryCreateAPIView,
                    QuestionRetrieveAPIView,)


urlpatterns = [
    path('diary/', DiaryCreateAPIView.as_view()),
    path('question/', QuestionRetrieveAPIView.as_view()),
    path('answer/', AnswerAPIView.as_view()),
]
