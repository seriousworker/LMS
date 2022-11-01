import datetime
from random import randint

from core.models import PersonModel
from core.models import SocialLinksBase

from dateutil.relativedelta import relativedelta

from django.db import models


class Teacher(PersonModel, SocialLinksBase):
    salary = models.PositiveIntegerField(null=True, blank=True)
    occupation = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    working_place = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        db_column='company'
    )

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        db_table = 'teachers'

    @classmethod
    def _generate(cls):
        obj = super()._generate()
        obj.salary = randint(10_000, 100_000)
        obj.save()
