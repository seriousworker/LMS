import datetime

from dateutil.relativedelta import relativedelta

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker


class BaseModel(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PersonModel(BaseModel):
    VALID_DOMAIN_LIST = ('@gmail.com', '@yahoo.com', '@test.com')
    VALID_PHONE_OPERATORS_CODES = ('38(067)', '38(098)', '38(063)', '38(050)', '38(039)',
                                   '38(093)', '38(096)', '38(097)', '38(068)', '38(092)',
                                   '38(094)', '38(091)', '38(066)', '38(095)', '38(099)')

    first_name = models.CharField(
        max_length=100,
        verbose_name='first name',
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': 'first_name field value less than two symbols'},
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='last name',
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': 'last_name field value less than two symbols'},
    )
    birthday = models.DateField(
        default=datetime.date.today,
        null=True,
        blank=True,
    )
    email = models.EmailField()
    phone = models.CharField(
        max_length=16,
        verbose_name='phone number',
        validators=[MinLengthValidator(16)],
        error_messages={'max_length': 'Phone number is too long, must be 12 digits!',
                        'min_length': 'Phone number is too short, must be 12 digits!'}
    )

    class Meta:
        abstract = True

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    @classmethod
    def _generate(cls):
        f = Faker()

        first_name = f.first_name()
        last_name = f.last_name()
        obj = cls(
            first_name=first_name,
            last_name=last_name,
            birthday=f.date_between(start_date='-65y', end_date='-15y'),
            email=f'{first_name}.{last_name}{f.random.choice(cls.VALID_DOMAIN_LIST)}',
            phone=f'{f.random.choice(PersonModel.VALID_PHONE_OPERATORS_CODES)}{f.random.randint(100, 999)}-'
                  f'{f.random.randint(10, 99)}-{f.random.randint(10, 99)}'
        )
        obj.save()
        return obj

    @classmethod
    def generator(cls, cnt):
        for _ in range(cnt):
            cls._generate()
