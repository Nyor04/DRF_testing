# Generated by Django 5.1.2 on 2024-11-07 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_appointment', '0002_rename_medicalnote_appointmentnote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='status',
        ),
        migrations.AddField(
            model_name='appointment',
            name='pending',
            field=models.BooleanField(default=True),
        ),
    ]