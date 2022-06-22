# Generated by Django 4.0.2 on 2022-02-25 01:54

from django.db import migrations, models
import django.db.models.deletion
import sampleapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='student', to='sampleapp.classes'),
        ),
        migrations.AddField(
            model_name='student',
            name='student_email',
            field=models.CharField(blank=True, max_length=40, null=True, unique=True, validators=[sampleapp.models.validate_email]),
        ),
        migrations.AddField(
            model_name='teachers',
            name='teachers_email',
            field=models.CharField(blank=True, max_length=40, null=True, unique=True, validators=[sampleapp.models.validate_email]),
        ),
        migrations.AlterField(
            model_name='class_teachers_bridge',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='class_teacher_bridge', to='sampleapp.teachers'),
        ),
        migrations.AlterField(
            model_name='classes',
            name='max_age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='classes',
            name='max_student',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='classes',
            name='min_age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='qualifications',
            field=models.CharField(max_length=100),
        ),
    ]