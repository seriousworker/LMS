# Generated by Django 4.1.1 on 2022-10-17 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_course_groups'),
        ('groups', '0007_group_headman'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Group', 'verbose_name_plural': 'Groups'},
        ),
        migrations.AddField(
            model_name='group',
            name='course',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_of_course', to='courses.course'),
        ),
    ]
