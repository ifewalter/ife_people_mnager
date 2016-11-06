__author__ = 'ife'

from django import forms

class AddForm(forms.Form):
    error_css_class = 'text-danger'

    full_name = forms.CharField(label='Fullame', max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email_address = forms.EmailField(label='Email Address', max_length=254, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))