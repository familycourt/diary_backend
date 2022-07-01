from rest_framework import serializers
from rest_framework import fields
from rest_framework.fields import (BooleanField, CharField,
                                   IntegerField,
                                   FloatField,
                                   DateField,
                                   SerializerMethodField,
                                   )
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import PrimaryKeyRelatedField

from .models import Diary, Question, Answer, Comment
