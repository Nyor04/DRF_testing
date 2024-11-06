# Generated by Django 5.1.2 on 2024-11-03 22:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('medical_history', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MediacalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('diagnosis', models.TextField()),
                ('treatment', models.TextField()),
                ('follow_up_date', models.DateField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_records', to='app_patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=125)),
                ('policy_number', models.CharField(max_length=100)),
                ('expiration_date', models.DateField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurances', to='app_patient.patient')),
            ],
        ),
    ]