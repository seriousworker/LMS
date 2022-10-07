from core.utils import clean_phone_number

from django.core.exceptions import ValidationError

import students.models


def validate_unique_email(value):
    mails_from_db = students.models.Student.objects.filter(email=value)

    if len(mails_from_db) > 0:
        raise ValidationError(f'Entered email - {value} already exist')


def validate_unique_phone_number(value):
    cleaned_number = clean_phone_number(value)
    phone_numbers_from_base = students.models.Student.objects.filter(phone=cleaned_number)

    if len(phone_numbers_from_base) > 0:
        raise ValidationError(f'Entered phone number - {cleaned_number} already exist')
