# Generated by Django 4.0.2 on 2022-03-04 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0003_qualification_teachers_years_exeperience_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teachers',
            old_name='years_exeperience',
            new_name='years_experience',
        ),
    ]