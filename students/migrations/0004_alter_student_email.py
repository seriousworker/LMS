# Generated by Django 4.1.1 on 2022-10-19 16:04

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(error_messages={'invalid': 'Entered email domain not valid'}, max_length=254, validators=[core.validators.valid_email_domain]),
        ),
    ]