from django import forms
from django.contrib.auth.models import User
from django.forms.fields import DateField

from .models import PrivateGoal


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class PrivateGoalCreateForm(forms.ModelForm):
    goalName = forms.CharField(label='Name')
    goalInitialDate = DateField(label='Initial Date', widget=forms.SelectDateWidget())
    goalDeadline = DateField(label='Deadline', widget=forms.SelectDateWidget())

    class Meta:
        model = PrivateGoal
        fields = 'goalName', 'goalInitialDate', 'goalDeadline'
