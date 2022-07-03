from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, ValidationError, PermissionDenied

from apps.diary.models import Diary
from .serializers import DiaryWriteSerializer


class DiaryCreateAPIView(CreateAPIView):
    serializer_class = DiaryWriteSerializer


class DiaryRegisterAPIView(APIView):
    def post(self, request):
        try:
            code = request.data['code']
        except KeyError:
            raise ParseError('Registraion code is not given')
        try:
            diary = Diary.objects.get(code=code)
        except Diary.DoesNotExist:
            raise ValidationError(
                'Diary with given Registration code does not exists')
        if request.user in diary.users.all():
            raise ValidationError('This user is already in this diary')
        diary.users.add(request.user)
        diary.save()
        return Response('Succesfully registered')


class DiaryCodeAPIView(APIView):
    def get(self, request):
        try:
            diary = Diary.objects.get(id=request.query_params['diary'])
        except KeyError:
            raise ParseError('Diary id is not given')
        except ValueError:
            raise ParseError('Diary id should be in decimal format')
        except Diary.DoesNotExist:
            raise ParseError('Diary with given id does not exists')
        if diary.admin != request.user:
            raise PermissionDenied(
                'You are not allowed to get this diary\'s code')
        return Response({'code': diary.code})
