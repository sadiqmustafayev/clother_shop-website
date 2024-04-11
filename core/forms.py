from django import forms
from core.models import Contact


class ContactUsForm(forms.ModelForm):

  class Meta:
    model = Contact
    fields = ['name', 'email','message']
    widgets = {
      'name':
      forms.TextInput(
        attrs={
          'class': 'form-control',
          'placeholder': 'Name',
          'pattern': '[A-Za-z]+',
          'title': 'Only alphabetical characters are allowed.'
        }),
      'email':
      forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
      }),
      'message':
      forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3,
        'placeholder': 'Message'
      })
    }
