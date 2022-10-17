# Generated by Django 4.1.1 on 2022-10-14 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_group_end_date_group_start_date_and_more'),
        ('students', '0010_remove_student_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='groups.group'),
        ),
    ]