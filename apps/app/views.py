from rest_framework.generics import (CreateAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response

from .serializers import DiarySerializer, DiaryWriteSerializer
from .models import Diary, Question, Answer, Comment


class DiaryCreateAPIView(CreateAPIView):
    serializer_class = DiaryWriteSerializer
    queryset = Diary.objects.all()
