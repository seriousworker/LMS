import datetime

from core.validators import ValidEmailDomain
from core.validators import ValidateOperatorCode
from core.validators import min_len_phone_number_validate

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from .validators import validate_unique_email
from .validators import validate_unique_phone_number

VALID_DOMAIN_LIST = ('@gmail.com', '@yahoo.com', '@test.com')
VALID_PHONE_OPERATORS_CODES = ('38(067)', '38(098)', '38(063)', '38(050)', '38(039)',
                               '38(093)', '38(096)', '38(097)', '38(068)', '38(092)',
                               '38(094)', '38(091)', '38(066)', '38(095)', '38(099)')


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

    # we use validation class here because we'll send parameters
    email = models.EmailField(validators=[ValidEmailDomain(*VALID_DOMAIN_LIST), validate_unique_email])
    phone = models.CharField(
        max_length=16,
        verbose_name='phone number',
        validators=[min_len_phone_number_validate, ValidateOperatorCode(*VALID_PHONE_OPERATORS_CODES),
                    validate_unique_phone_number],
        error_messages={'max_length': 'Phone number is too long, must be 12 digits!'}
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'students'

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()

        for _ in range(cnt):
            first_name = f.first_name()
            last_name = f.last_name()
            email = f'{first_name}.{last_name}{f.random.choice(VALID_DOMAIN_LIST)}'
            birthday = f.date()
            phone = f'{f.random.choice(VALID_PHONE_OPERATORS_CODES)}{f.random.randint(100, 999)}-' \
                    f'{f.random.randint(10, 99)}-{f.random.randint(10, 99)}'
            st = cls(first_name=first_name, last_name=last_name, birthday=birthday, email=email, phone=phone)

            try:
                st.full_clean()
                st.save()
            except Exception:
                print(f'Incorrect data {first_name} {last_name} {email} {birthday} {phone}')
