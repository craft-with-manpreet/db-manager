# Author: Manpreet Singh
# Email: dev.manpreet.io@gmail.com
# GitHub: https://github.com/craft-with-manpreet
# Portfolio: https://dev-manpreet.web.app
from django import forms
from database_management import models


class DatabaseForm(forms.ModelForm):
    class Meta:
        model = models.Database
        fields = "__all__"


class ScheduleBackupForm(forms.ModelForm):
    class Meta:
        model = models.BackupSchedule
        exclude = ("database",)
