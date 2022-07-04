from rest_framework.serializers import Serializer, ModelSerializer, ValidationError
from rest_framework.fields import (CharField,
                                   IntegerField,)
from .models import Question, Answer, Comment


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
    id = CharField()
    user = CharField(source='user.name')
    question = CharField(source='question.content')
    content = CharField()
    year = IntegerField()


class CommentSerializer(ModelSerializer):
    user = CharField(source='user.name', read_only=True)
    answer_id = CharField(source='answer.id', read_only=True)

    class Meta:
        model = Comment
        exclude = ['id', ]

    def create(self, validated_data):
        return Comment.objects.create(user=self.context['request'].user, **validated_data)

    def validate(self, attrs):
        user = self.context['request'].user
        if attrs['answer'].diary not in user.diaries.all():
            raise ValidationError(
                'This user is not allowed to write in this diary')
        return super().validate(attrs)
