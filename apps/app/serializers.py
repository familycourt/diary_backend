import uuid
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import fields
from rest_framework.fields import (BooleanField,
                                   CharField,
                                   IntegerField,
                                   FloatField,
                                   DateField,
                                   SerializerMethodField,)
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import PrimaryKeyRelatedField

from .models import Diary, Question, Answer, Comment


class DiaryWriteSerializer(Serializer):

    def create(self, validated_data):
        diary = Diary.objects.create(
            admin=self.context['request'].user,
            code=str(uuid.uuid4())
        )
        diary.users.add(self.context['request'].user)
        return diary


class DiarySerializer(ModelSerializer):

    class Meta:
        model = Diary
        fields = '__all__'


class QuestionSerializer(ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'


class AnswerListSerializer(Serializer):
    user = CharField(source='user.username')
    question = CharField(source='question.content')
    content = CharField()
    year = IntegerField()


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
