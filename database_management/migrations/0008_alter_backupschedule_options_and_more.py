# Generated by Django 5.0.6 on 2024-08-28 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database_management', '0007_backupschedule'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='backupschedule',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RenameField(
            model_name='backupschedule',
            old_name='granularity',
            new_name='frequency',
        ),
        migrations.AlterUniqueTogether(
            name='backupschedule',
            unique_together={('database', 'frequency')},
        ),
    ]