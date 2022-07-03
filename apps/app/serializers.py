import uuid
from rest_framework.serializers import Serializer, ModelSerializer, ValidationError
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
        exclude = ['user', ]

    def create(self, validated_data):
        return Answer.objects.create(user=self.context['request'].user, **validated_data)

    def validate(self, attrs):
        user = self.context['request'].user
        if attrs['diary'] not in user.diaries.all():
            raise ValidationError(
                'This user is not allowed to write in this diary')
        if Answer.objects.filter(user=user, **attrs).first():
            raise ValidationError(
                'This user already answered to this question')
        return super().validate(attrs)


class AnswerListSerializer(Serializer):
    user = CharField(source='user.username')
    question = CharField(source='question.content')
    content = CharField()
    year = IntegerField()


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
