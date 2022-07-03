from django.db import models
from django.contrib.auth import get_user_model


class Question(models.Model):
    content = models.CharField(max_length=256)
    month = models.IntegerField(null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)


class Answer(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    diary = models.ForeignKey('diary.Diary', on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    year = models.IntegerField()


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
