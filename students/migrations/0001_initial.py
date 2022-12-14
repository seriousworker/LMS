# Generated by Django 4.1.1 on 2022-11-05 08:13

import core.validators
import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(error_messages={'min_length': 'first_name field value less than two symbols'}, max_length=100, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='first name')),
                ('last_name', models.CharField(error_messages={'min_length': 'last_name field value less than two symbols'}, max_length=100, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='last name')),
                ('birthday', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('phone', models.CharField(error_messages={'max_length': 'Phone number is too long, must be 12 digits!', 'min_length': 'Phone number is too short, must be 12 digits!'}, max_length=16, validators=[django.core.validators.MinLengthValidator(16)], verbose_name='phone number')),
                ('email', models.EmailField(max_length=254, validators=[core.validators.valid_email_domain])),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='groups.group')),
            ],
            options={
                'db_table': 'students',
            },
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkedin', models.CharField(blank=True, db_column='LinkedIn', max_length=500, null=True)),
                ('telegram', models.CharField(blank=True, db_column='Telegram', max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, db_column='Facebook', max_length=100, null=True)),
                ('youtube', models.CharField(blank=True, db_column='YouTube', max_length=100, null=True)),
                ('instagram', models.CharField(blank=True, db_column='Instagram', max_length=100, null=True)),
                ('student', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_links', to='students.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
