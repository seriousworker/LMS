# Generated by Django 4.1.1 on 2022-09-27 11:58

from django.db import migrations, models
import students.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(error_messages={'max_length': 'Phone number is too long, must be 12 digits!'}, max_length=16, validators=[students.validators.min_len_phone_number_validate, students.validators.ValidateOperatorCode('067', '098', '063', '050', '039', '093', '096', '097', '068', '092', '094', '091', '066', '095', '099'), students.validators.validate_unique_phone_number], verbose_name='phone number'),
        ),
    ]