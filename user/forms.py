from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms.widgets import SelectDateWidget
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField
from .models import MyUser
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


#registration form
class UserForm(UserCreationForm):
  email = forms.EmailField(
    max_length=35,
    help_text=_('Required. Enter a valid email address.'),
    widget=forms.EmailInput(attrs={
      'class': 'form-control',
      'placeholder': 'Email'
    }))

  first_name = forms.CharField(
    max_length=30,
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder': _('First Name'),
        'pattern': '[A-Za-z]+',
        'title': _('Only alphabetical characters are allowed.')
      }))

  last_name = forms.CharField(
    max_length=30,
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder': _('Last Name'),
        'pattern': '[A-Za-z]+',
        'title': _('Only alphabetical characters are allowed.')
      }))

  password1 = forms.CharField(
    strip=False,
    widget=forms.PasswordInput(attrs={
      'class': 'form-control',
      'placeholder': _('Password')
    }),
  )
  #help_text='Your password must contain at least 8 characters, at least one digit, and can\'t be entirely alphabetical or entirely numeric.')

  password2 = forms.CharField(
    strip=False,
    widget=forms.PasswordInput(attrs={
      ''
      'class': 'form-control',
      'placeholder': _('Confirm Password')
    }),
    help_text=_('Enter the same password as before, for verification.'))

  class Meta:
    model = MyUser
    fields = [
      'username',
      'email',
      'first_name',
      'last_name',
      'password1',
      'password2',
      'phone_number', 
      'address',
      'country',
      'city', 
      'zip_code', 
      'date_of_birth',
    ]
    labels = {
    'password2': 'Writer',
    }
    widgets = {
      'username':
      forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
      }),
    }

  def clean_password1(self):
    password1 = self.cleaned_data.get('password1')
    if len(password1) < 8:
      raise forms.ValidationError(
        _("Your password must contain at least 8 characters."))
    elif any(char.isdigit() for char in password1) == False:
      raise forms.ValidationError(
        _("Your password must contain at least one digit."))
    elif password1.isalpha():
      raise forms.ValidationError(
        _("Your password can't be entirely alphabetical."))
    elif password1.isnumeric():
      raise forms.ValidationError(
        _("Your password can't be entirely numeric."))
    elif not password1[0].isupper():
      raise forms.ValidationError(
        _("Your password must start with a capital letter."))
    return password1


#login form
class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(
    attrs={
      'class': 'form-control',
      'placeholder': 'Username'
    }))
  password = forms.CharField(widget=forms.PasswordInput(
    attrs={
      'class': 'form-control',
      'placeholder': 'Password'
    }))


User = get_user_model()


#update
class UserUpdateForm(forms.ModelForm):
  first_name = forms.CharField(
    label=(''),
    validators=[
      RegexValidator(
        regex=r'^[a-zA-Z]+$',
        message=_('Please enter only alphabets for your first name'),
        code='invalid_first_name')
    ],
    widget=forms.TextInput(attrs={
      'class': 'form-control',
      'placeholder': _('First Name')
    }))

  last_name = forms.CharField(
    label=(''),
    validators=[
      RegexValidator(
        regex=r'^[a-zA-Z]+$',
        message=_('Please enter only alphabets for your last name'),
        code='invalid_last_name')
    ],
    widget=forms.TextInput(attrs={
      'class': 'form-control',
      'placeholder': _('Last Name')
    }))

  email = forms.EmailField(
    label=(''),
    widget=forms.EmailInput(attrs={
      'class': 'form-control',
      'placeholder': _('Email Address')
    }))
  date_of_birth = forms.DateField(
    label=(''),
    widget=forms.DateInput(attrs={
      'class': 'form-control',
      'type': 'date',
      'input_formats': ['%d-%m-%Y'],
    }))

  phone_number = PhoneNumberField(
    label=(''),
    widget=forms.TextInput(attrs={
      'class': 'form-control',
      'placeholder': _('Phone Number')
    }))

  location = forms.CharField(
    label=(''),
    widget=forms.TextInput(attrs={
      'class': 'form-control',
      'placeholder': _('Location')
    }))

  password = forms.CharField(
    label=(''),
    widget=forms.PasswordInput(
      attrs={
        'autocomplete': 'new-password',
        'class': 'form-control',
        'placeholder': _('New Password')
      }),
    required=False,
    help_text=_(
      _('Optional. Enter a strong password with at least 8 characters.')),
    validators=[
      RegexValidator(
        regex=r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$',
        message=_(
          _('Password must contain at least 8 characters with at least one uppercase letter, one lowercase letter, and one digit.'
            )),
        code=_('invalid_password'))
    ])

  password_confirmation = forms.CharField(
    label=(''),
    widget=forms.PasswordInput(
      attrs={
        'autocomplete': 'new-password',
        'class': 'form-control',
        'placeholder': _('Confirm Password')
      }),
    required=False,
    help_text=_('Optional. Re-enter the password to confirm.'),
  )

  class Meta:
    model = MyUser
    fields = [
      'first_name', 'last_name', 'email', 'date_of_birth', 'phone_number',
      'location'
    ]

  def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get('password')
    password_confirmation = cleaned_data.get('password_confirmation')

    if password and not password_confirmation:
      self.add_error('password_confirmation', _('This field is required.'))

    if password_confirmation and not password:
      self.add_error('password', _('This field is required.'))

    if password and password_confirmation and password != password_confirmation:
      raise forms.ValidationError(
        _('Passwords do not match. Please try again.'))

    return cleaned_data
