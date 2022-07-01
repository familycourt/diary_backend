from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, password=None):
        if not username:
            raise ValidationError('Username must be given.')

        user = User(username=username, password=None)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password=None):
        superuser = self.create_user(username, password)
        superuser.is_staff = True
        superuser.save()

        return superuser


class User(AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.username)

    def has_perm(self, obj):
        return True

    def has_module_perms(self, obj):
        return True
