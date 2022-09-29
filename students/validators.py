from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

import students.models
from students.utils import clean_phone_number


def valid_email_domain(value):
    valid_domains = ['@gmail.com', '@yahoo.com']

    for domain in valid_domains:
        if domain in value:
            break
    else:
        raise ValidationError(f'Email <{value}> is incorrect address.')


@deconstructible
class ValidEmailDomain:
    def __init__(self, *domains):
        self.domains = list(domains)

    def __call__(self, *args, **kwargs):
        for domain in self.domains:
            if args[0].endswith(domain):
                break
        else:
            raise ValidationError(f'Invalid email address. The domain <{args[0].split("@")[1]}> not valid.')


@deconstructible
class ValidateOperatorCode:
    def __init__(self, *codes):
        self.valid_codes = list(codes)

    def __call__(self, *args, **kwargs):
        self.clean_number = clean_phone_number(args[0])

        for code in self.valid_codes:
            if self.clean_number.startswith(code):
                break
        else:
            raise ValidationError('Either entered operator or country code not valid!')


def min_len_phone_number_validate(value):
    cleaned_number = clean_phone_number(value)

    if len(cleaned_number) < 16:
        raise ValidationError('Phone number is too short, must be 12 digits!')


def validate_unique_email(value):
    mails_from_db = students.models.Student.objects.filter(email=value)

    if len(mails_from_db) > 0:
        raise ValidationError(f'Entered email - {value} already exist')


def validate_unique_phone_number(value):
    cleaned_number = clean_phone_number(value)
    phone_numbers_from_base = students.models.Student.objects.filter(phone=cleaned_number)

    if len(phone_numbers_from_base) > 0:
        raise ValidationError(f'Entered phone number - {cleaned_number} already exist')
