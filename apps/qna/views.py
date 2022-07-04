from urllib import request
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, ValidationError

from .serializers import (
    AnswerSerializer,
    AnswerListSerializer,
    CommentSerializer,
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

    def get_queryset(self):
        question = get_question_object(self.request.query_params.get('date'))
        try:
            year = int(self.request.query_params['year'])
            diary = int(self.request.query_params['diary'])
        except KeyError:
            raise ParseError('Year, Diary id not given')
        except ValueError:
            raise ParseError('Year and Diary id should be in decimal format')
        if diary not in [d.id for d in self.request.user.diaries.all()]:
            raise ValidationError(
                'This user is not allowed to read from this diary')
        return Answer.objects.filter(
            user=self.request.user, question=question, diary_id=diary, year=year)


class CommentAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        try:
            answer = Answer.objects.get(
                id=int(self.request.query_params['answer']))
            queryset = Comment.objects.filter(answer=answer)
        except KeyError:
            raise ParseError('Answer id is not given')
        except ValueError:
            raise ParseError('Answer id should be in decimal format')
        except Answer.DoesNotExist:
            raise ParseError('Answer with given id does not exists')
        if answer.diary not in self.request.user.diaries.all():
            raise ValidationError(
                'This user is not allowed to read from this diary')
        return queryset
