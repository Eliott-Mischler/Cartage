# Generated by Django 4.0.1 on 2022-01-18 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartage', '0004_trip_madebyteacher_trip_student_trip_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='madeByTeacher',
        ),
    ]