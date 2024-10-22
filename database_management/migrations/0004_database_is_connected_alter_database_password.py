# Author: Manpreet Singh
# Email: dev.manpreet.io@gmail.com
# GitHub: https://github.com/craft-with-manpreet
# Portfolio: https://dev-manpreet.web.app
# Generated by Django 5.0.6 on 2024-08-26 14:34

import encrypted_model_fields.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('database_management', '0003_alter_database_options_database_database_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='database',
            name='is_connected',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='password',
            field=encrypted_model_fields.fields.EncryptedCharField(blank=True),
        ),
    ]
