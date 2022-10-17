import datetime

from core.validators import validate_start_date

from django.core.validators import MinLengthValidator
from django.db import models


class Group(models.Model):
    group_name = models.CharField(
        max_length=50,
        verbose_name='Group name',
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': 'group_name field value less than two symbols'},
    )
    group_creation_date = models.DateField(
        auto_now_add=True,
        validators=[validate_start_date],
    )
    start_date = models.DateField(
        default=datetime.datetime.utcnow,
    )
    end_date = models.DateField(
        null=True,
        blank=True,
    )
    update_datetime = models.DateTimeField(auto_now=True)
    headman = models.OneToOneField(
        'students.Student',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headman_group',
    )
    course = models.OneToOneField(
        'courses.Course',
        null=True,
        on_delete=models.CASCADE,
        related_name='group_of_course',
    )

    def __str__(self):
        return f'group {self.group_name}, created {self.group_creation_date}'

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
        db_table = 'groups'
