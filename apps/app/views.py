from rest_framework.views import APIView
from rest_framework.generics import (CreateAPIView,
                                     GenericAPIView,
                                     RetrieveAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from .serializers import AnswerSerializer, DiarySerializer, DiaryWriteSerializer, QuestionSerializer
from .models import Diary, Question, Answer, Comment


def get_question_object(date):
    try:
        month, day = [int(x) for x in date.strip().split('-')]
    except AttributeError:
        raise ParseError('Date is not given')
    except ValueError:
        raise ParseError('Date should be in "[Month]-[Date]" format')
    try:
        question = Question.objects.get(month=month, day=day)
    except Question.DoesNotExist:
        raise ParseError('Question with given date does not exists')
    return question


class DiaryCreateAPIView(CreateAPIView):
    serializer_class = DiaryWriteSerializer


class QuestionRetrieveAPIView(APIView):
    def get(self, request):
        question = get_question_object(request.query_params.get('date'))
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
