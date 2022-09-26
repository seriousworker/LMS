import datetime

from django.core.exceptions import ValidationError


def validate_start_date(value):
    if value < datetime.date.today():
        raise ValidationError(f"Entered date {value} not valid, past dates can't be set")
