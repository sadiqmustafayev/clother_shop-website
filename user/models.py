from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class MyUser(AbstractUser):
  phone_number = PhoneNumberField(blank=True)
  address = models.CharField(max_length=255)
  country = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  zip_code = models.CharField(max_length=10)
  updated_at = models.DateTimeField(auto_now=True)
  date_of_birth = models.DateField(null=True, blank=True)
  email = models.EmailField(max_length=255, unique=True)

