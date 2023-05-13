from django import forms
from django.forms import ModelForm
from .models import MailOrPhone, MailPass, PhoneNum


class MailForm(forms.ModelForm):
    
    class Meta:
        model = MailOrPhone
        fields = "__all__"


class PassForm(forms.ModelForm):
    
    class Meta:
        model = MailPass
        fields = "__all__"


class PhoneNumForm(ModelForm):
    
    class Meta:
        model = PhoneNum
        fields = '__all__'
