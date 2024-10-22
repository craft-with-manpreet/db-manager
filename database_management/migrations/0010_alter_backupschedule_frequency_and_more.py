# Generated by Django 5.0.6 on 2024-08-28 13:21

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_management', '0009_alter_backupschedule_database'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backupschedule',
            name='frequency',
            field=models.CharField(choices=[('hourly', 'Hourly'), ('everyday', 'Everyday'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], max_length=10),
        ),
        migrations.AlterField(
            model_name='backupschedule',
            name='id',
            field=models.TextField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
