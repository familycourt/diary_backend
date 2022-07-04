from django.urls import path

from .views import AnswerAPIView, CommentAPIView, QuestionRetrieveAPIView


urlpatterns = [
    path('question/', QuestionRetrieveAPIView.as_view()),
    path('answer/', AnswerAPIView.as_view()),
    path('comment/', CommentAPIView.as_view()),
]
