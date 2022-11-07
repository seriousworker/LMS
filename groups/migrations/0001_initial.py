# Generated by Django 4.1.1 on 2022-11-05 08:13

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('group_name', models.CharField(error_messages={'min_length': 'group_name field value less than two symbols'}, max_length=50, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Group name')),
                ('start_date', models.DateField(default=datetime.datetime.utcnow)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('course', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_of_course', to='courses.course')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'db_table': 'groups',
            },
        ),
    ]
