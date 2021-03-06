# Generated by Django 4.0.1 on 2022-01-18 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cartage', '0005_remove_trip_madebyteacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_user', to='cartage.user'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_user', to='cartage.user'),
        ),
    ]
