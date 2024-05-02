from django import forms
from core.models import Contact, ShopComments


class ContactForm(forms.ModelForm):

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




class CommentForm(forms.ModelForm):
    class Meta:
        model = ShopComments
        fields = ['name', 'email', 'phone_number', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Comment'}),
        }