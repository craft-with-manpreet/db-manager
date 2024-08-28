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
        exclude = ("id", "database",)

    def clean(self):
        super(ScheduleBackupForm, self).clean()
        value = self.cleaned_data["frequency"]
        database = self.initial["database"]
        instance = self.instance
        if instance:
            if models.BackupSchedule.objects.filter(database=database, frequency=value).exclude(
                    id=instance.id
            ).exists():
                raise forms.ValidationError({"frequency": ["Schedule already exists"]})
        else:
            if models.BackupSchedule.objects.filter(database=database, frequency=value).exists():
                raise forms.ValidationError({"frequency": ["Schedule already exists"]})

        return self.cleaned_data
