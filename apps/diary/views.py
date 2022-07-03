from rest_framework.generics import CreateAPIView
from .serializers import DiaryWriteSerializer


class DiaryCreateAPIView(CreateAPIView):
    serializer_class = DiaryWriteSerializer
