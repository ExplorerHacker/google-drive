from django import forms
from django.forms import ModelForm
from .models import MailOrPhone, MailPass, PhoneNum
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from phonenumber_field.formfields import PhoneNumberField


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
        # widgets = {
        #     'phone': PhoneNumberPrefixWidget(),
        # }
