from django.db import models
from django.contrib.auth import get_user_model


class Diary(models.Model):
    admin = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    users = models.ManyToManyField(get_user_model(), related_name='diaries')
    code = models.CharField(max_length=128, unique=True)
