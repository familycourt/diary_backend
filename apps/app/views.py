from rest_framework.views import APIView
from rest_framework.generics import (CreateAPIView,
                                     GenericAPIView,
                                     RetrieveAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from .serializers import DiarySerializer, DiaryWriteSerializer, QuestionSerializer
from .models import Diary, Question, Answer, Comment


class DiaryCreateAPIView(CreateAPIView):
    serializer_class = DiaryWriteSerializer


class QuestionRetrieveAPIView(APIView):
    def get(self, request):
        try:
            month, day = request.query_params.get('date').strip().split('-')
        except AttributeError:
            raise ParseError('Date is not given.')
        except ValueError:
            raise ParseError('Date should be in "Month-Date" format')
        queryset = Question.objects.filter(month=int(month), day=int(day))
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)
