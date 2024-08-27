from django import forms
from database_management import models


class DatabaseForm(forms.ModelForm):
    class Meta:
        model = models.Database
        fields = "__all__"
