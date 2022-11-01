import random

from core.models import PersonModel
from core.models import SocialLinksBase
from core.validators import valid_email_domain

from django.db import models

from groups.models import Group


class Student(PersonModel):
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        null=True,
        related_name='students'
    )
    email = models.EmailField(
        validators=[valid_email_domain],
    )

    def __str__(self):
        if self.group is None:
            return f'{self.first_name} {self.last_name}'
        else:
            return f'{self.first_name} {self.last_name} ({self.group.group_name})'

    class Meta:
        db_table = 'students'

    @classmethod
    def _generate(cls):
        obj = super()._generate()
        groups = Group.objects.all()
        obj.group = random.choice(groups)
        obj.save()


class SocialLinks(SocialLinksBase):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='student_links',
    )
