from django import forms
from .models import SignUp


class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()


class SignUpForm(forms.ModelForm):

    class Meta:
        model = SignUp
        fields = ["email", "full_name"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, provider = email.split("@")
        domain, extension = provider.split(".")
        # if not domain == "syr":
        #     raise forms.ValidationError("Please make sure using 'syr'")
        # if not extension == "gov":
        #     raise forms.ValidationError("Please enter '.gov' domain")
        return email

    def clean_fullname(self):
        full_name = self.cleaned_data.get("full_name")
        return full_name
