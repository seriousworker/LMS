import datetime

from django.core.validators import MinLengthValidator
from django.db import models

from groups.validators import validate_start_date


class Group(models.Model):
    group_name = models.CharField(
        max_length=50,
        verbose_name='Group name',
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': 'group_name field value less than two symbols'}
    )
    group_creation_date = models.DateField(default=datetime.date.today, validators=[validate_start_date])
    group_description = models.TextField(
        max_length=300,
        verbose_name='Group description',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'group {self.group_name} created {self.group_creation_date}, description {self.group_description}'

    class Meta:
        db_table = 'groups'
