from django.forms import ModelForm
from django import forms
from pollresults.models import Lead
from django.contrib.auth.models import User


# We put all of our forms here

class LeadForm(ModelForm):
    class Meta:
        model = Lead


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')