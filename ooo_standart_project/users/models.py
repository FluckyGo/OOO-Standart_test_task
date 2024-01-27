from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

from api.constants import (
    REQUIRED_FIELDS, MAX_USER_MODEL_FIELD_LENGTH, USER, USER_ROLES)


class CustomUser(AbstractUser):
    """ Кастомная модель пользователя. """

    REQUIRED_FIELDS = REQUIRED_FIELDS

    username = models.CharField(
        'Логин',
        max_length=MAX_USER_MODEL_FIELD_LENGTH,
        unique=True,
        validators=[UnicodeUsernameValidator()]
    )

    password = models.CharField(
        'Пароль', max_length=MAX_USER_MODEL_FIELD_LENGTH)

    first_name = models.CharField(
        'Имя', max_length=MAX_USER_MODEL_FIELD_LENGTH)
    last_name = models.CharField(
        'Фамилия', max_length=MAX_USER_MODEL_FIELD_LENGTH)

    role = models.CharField('Роль', max_length=50,
                            choices=USER_ROLES, default=USER)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.username
