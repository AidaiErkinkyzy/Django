from django import forms
from .models import *



class ContactUsForm(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Имя'
    }))
    email = forms.EmailField(widget = forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Email'
    }))
    phone = forms.CharField(widget = forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Телефон'
    }))
    message = forms.CharField(widget = forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Сообщение'
    }))


    class Meta :
        model = ContactUs
        fields = ('name', 'email', 'phone', 'message')



