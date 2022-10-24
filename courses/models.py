from core.models import BaseModel

from django.core.validators import MinLengthValidator
from django.db import models


class Course(BaseModel):
    course_title = models.CharField(
        max_length=50,
        verbose_name='Title',
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': 'course title field value less than two symbols'},
        db_column='title',
    )

    CITY = [
        (None, 'Choose a city'),
        ('k', 'Kyiv'),
        ('o', 'Odesa'),
        ('d', 'Dnieper'),
        ('h', 'Kharkiv'),
        ('l', 'Lviv'),
        ('v', 'Vinnitsa'),
        ('p', 'Poltava'),
    ]
    course_place = models.CharField(
        max_length=1,
        choices=CITY,
        default=None,
        verbose_name='Location',
        db_column='place'
    )

    LEVEL = [
        (None, 'Choose a level'),
        ('b', 'Basic'),
        ('a', 'Advanced'),
        ('p', 'Pro')
    ]
    course_level = models.CharField(
        max_length=1,
        choices=LEVEL,
        default=None,
        verbose_name='Level',
        db_column='level',
    )

    course_description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Teaching plan',
        db_column='description'
    )
    course_duration = models.SmallIntegerField(
        verbose_name='Duration',
        db_column='duration'
    )
    course_start = models.DateField(
        null=True,
        blank=True,
        verbose_name='Start date',
        db_column='star_date',
    )
    course_price = models.IntegerField(
        verbose_name='Price',
        db_column='price',
    )

    CURRENCY = [
        ('h', 'UAH'),
        ('d', 'USD'),
        ('e', 'EURO'),
    ]
    course_price_currency = models.CharField(
        max_length=1,
        choices=CURRENCY,
        default='h',
        verbose_name='Currency',
        db_column='currency',
    )

    # points required for enrollment
    course_enrollment_condition = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Conditions of enrollment',
        db_column='enroll',
    )
    # points required to graduate from the course
    course_graduation_condition = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Conditions of graduation',
        db_column='graduate'
    )

    def __str__(self):
        return f'{self.course_title} - {self.get_course_place_display()}, {self.course_start}'

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        db_table = 'courses'
