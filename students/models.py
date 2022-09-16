import datetime

from django.core.validators import MinLengthValidator
from django.db import models # noqa


class Student(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name='first name',
        validators=[MinLengthValidator(2, 'first_name field value less than two symbols')]
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='last name',
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': 'last_name field value less than two symbols'}

    )
    birthday = models.DateField(default=datetime.date.today, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
