from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView
from user.forms import UserForm, UserUpdateForm
from core.models import Setting
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import user_passes_test


def register(request):
  form = UserForm()
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=password)
      login(request, user)
      return redirect('home')
  context = {
    'setting': Setting.objects.first(),
    'title': "Register",
    'form': form,
  }
  return render(request, "register.html", context)




def login_view(request):
  context = {'setting': Setting.objects.first(), 'title': "Login"}

  if request.method == 'POST':
    form = LoginForm(request=request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('home')
  else:
    form = LoginForm()

  context['form'] = form
  return render(request, 'login.html', context)



@login_required
def profile_edit(request):
  if request.method == 'POST':
    form = UserUpdateForm(request.POST, instance=request.user)
    if form.is_valid():
      user = form.save(commit=False)
      password = form.cleaned_data.get('password')
      if password:
        user.set_password(password)
      user.save()
      messages.success(request, _('Your profile was updated successfully.'))
      return redirect('home')
  else:
    form = UserUpdateForm(instance=request.user)


#user status

  user = request.user
  if user.is_superuser:
    user_status = _("Superuser")
  elif user.is_staff:
    user_status = _("Staff")
  else:
    user_status = _("User")

  context = {
    'setting': Setting.objects.first(),
    'form': form,
    'title': f' Edit Profile - {request.user.username} - {user_status}',
  }

  return render(request, 'profile_edit.html', context)
from django.contrib import messages


@login_required
def delete_account(request):
  setting = Setting.objects.first()

  if request.method == 'POST':
    if request.POST.get('confirm_delete', '') == _('yes'):
      #staff ve super user silinmir burdan
      if not request.user.is_staff and not request.user.is_superuser:
        if request.user.check_password(request.POST.get('password', '')):
          # hesabi sil
          user = request.user
          user.delete()

          # silenden sonra homa_("Settings")
          logout(request)
          return redirect(reverse('home'))
        else:
          messages.error(request, _('Your password is incorrect.'))
      else:
        messages.error(request,
                       _('You do not have permission to delete this account.'))
    else:
      messages.error(
        request, _('You must confirm that you want to delete your account.'))

  context = {
    'setting': setting,
    'email_attrs': {
      'class': 'form-control',
      'placeholder': _('Password')
    },
    'messages':
    messages.get_messages(request),  
  }

  return render(request, 'delete_account.html', context)
