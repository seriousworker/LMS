
import datetime

from dateutil.relativedelta import relativedelta

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

VALID_PHONE_OPERATORS_CODES = ('38(067)', '38(098)', '38(063)', '38(050)', '38(039)',
                               '38(093)', '38(096)', '38(097)', '38(068)', '38(092)',
                               '38(094)', '38(091)', '38(066)', '38(095)', '38(099)')


class Teacher(models.Model):
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
    subject = models.CharField(
        max_length=200,
        verbose_name='subject',
        default='IT teacher',
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': 'subject field value less than two symbols'},
    )
    email = models.EmailField()
    phone = models.CharField(
        max_length=16,
        verbose_name='phone number',
        validators=[MinLengthValidator(16)],
        error_messages={'max_length': 'Phone number is too long, must be 12 digits!',
                        'min_length': 'Phone number is too short, must be 12 digits!'}
    )

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'teachers'

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()

        for _ in range(cnt):
            first_name = f.first_name()
            last_name = f.last_name()
            email = f.email()
            birthday = f.date()
            subject = f.job()
            phone = f'{f.random.choice(VALID_PHONE_OPERATORS_CODES)}{f.random.randint(100, 999)}-' \
                    f'{f.random.randint(10, 99)}-{f.random.randint(10, 99)}'
            st = cls(first_name=first_name, last_name=last_name, birthday=birthday,
                     subject=subject, email=email, phone=phone)

            try:
                st.full_clean()
                st.save()
            except Exception:
                print(f'Incorrect data {first_name} {last_name} {birthday} {subject} {email} {phone}')
