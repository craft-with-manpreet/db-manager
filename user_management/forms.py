from django import forms
from django.contrib.auth.models import auth


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Please enter your email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Please enter your password"}),
                               min_length=6, max_length=20)

    def clean(self):
        super(LoginForm, self).clean()

        email: str = self.cleaned_data["email"]
        password: str = self.cleaned_data["password"]

        user = auth.authenticate(username=email, password=password, is_superuser=True, is_staff=True)
        if not user:
            self._errors["password"] = self.error_class(["Invalid email or password"])

        return self.cleaned_data
