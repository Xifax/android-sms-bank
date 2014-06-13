# coding: utf-8
from django import forms


class SMSForm(forms.Form):
    phone = forms.RegexField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        regex=r'^\+?1?\d{9,15}$',
        error_message = (u'Указан неправильный номер')
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
