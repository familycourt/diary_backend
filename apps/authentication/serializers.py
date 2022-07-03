from wsgiref.validate import validator
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from rest_framework.serializers import Serializer, ValidationError
from rest_framework.fields import CharField
from rest_framework.validators import UniqueValidator


class UserSerializer(Serializer):
    username = CharField(write_only=True, required=True,
                         max_length=32, min_length=8,
                         validators=[UniqueValidator(get_user_model().objects.all())])
    name = CharField(write_only=True, required=True, max_length=32)
    password = CharField(write_only=True, required=True,
                         validators=[validate_password])
    password2 = CharField(write_only=True, required=True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise ValidationError('Password fields does not match.')

        return data

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'], name=validated_data['name'])
        user.set_password(validated_data['password'])
        user.save()

        return user
