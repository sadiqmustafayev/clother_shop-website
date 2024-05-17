from django import forms
from core.models import Contact, ShopComments, BlogComments, Subscriber


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


class ShopCommentForm(forms.ModelForm):
    class Meta:
        model = ShopComments
        fields = ['name', 'email', 'phone_number', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'style': 'color: black;'})
        self.fields['email'].widget.attrs.update({'style': 'color: black;'})
        self.fields['phone_number'].widget.attrs.update({'style': 'color: black;'})
        self.fields['comment'].widget.attrs.update({'style': 'color: black;'})



class SizeSelectionForm(forms.Form):
    selected_sizes = forms.MultipleChoiceField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], widget=forms.CheckboxSelectMultiple)


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComments
        fields = ['name', 'email', 'phone_number', 'comment']


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']