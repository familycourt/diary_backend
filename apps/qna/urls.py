from django.urls import path

from .views import AnswerAPIView, QuestionRetrieveAPIView


urlpatterns = [
    path('question/', QuestionRetrieveAPIView.as_view()),
    path('answer/', AnswerAPIView.as_view()),
]
