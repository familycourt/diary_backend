from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from .serializers import (
    AnswerSerializer,
    AnswerListSerializer,
    QuestionSerializer)
from .models import Question, Answer, Comment


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


class QuestionRetrieveAPIView(APIView):
    def get(self, request):
        question = get_question_object(request.query_params.get('date'))
        serializer = QuestionSerializer(question)
        return Response(serializer.data)


class AnswerAPIView(ListCreateAPIView):
    serializer_class = AnswerSerializer

    def list(self, request, *args, **kwargs):
        question = get_question_object(request.query_params.get('date'))
        try:
            year = int(request.query_params['year'])
            diary = int(request.query_params['diary'])
        except KeyError:
            raise ParseError('Year, Diary id not given')
        except ValueError:
            raise ParseError('Year and Diary id should be in decimal format')
        queryset = Answer.objects.filter(
            user=request.user, question=question, diary_id=diary, year=year)
        serializer = AnswerListSerializer(queryset, many=True)
        print(queryset)
        return Response(serializer.data)
