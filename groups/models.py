import datetime

from core.models import BaseModel

from django.core.validators import MinLengthValidator
from django.db import models

from teachers.models import Teacher


class Group(BaseModel):
    group_name = models.CharField(
        max_length=50,
        verbose_name='Group name',
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': 'group_name field value less than two symbols'},
    )
    start_date = models.DateField(
        default=datetime.datetime.utcnow,
    )
    end_date = models.DateField(
        null=True,
        blank=True,
    )
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
    teachers = models.ManyToManyField(
        to=Teacher,
        null=True,
        blank=True,
        related_name='groups'
    )

    def __str__(self):
        return f'group {self.group_name}, created {self.created_datetime}'

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
        db_table = 'groups'

    @classmethod
    def generate_group(cls):
        groups = [
            'G1',
            'G2',
            'G3',
            'G4',
            'G5',
        ]

        for group in groups:
            Group.objects.create(
                group_name=group
            )
