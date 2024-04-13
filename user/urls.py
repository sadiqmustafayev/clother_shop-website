from django.urls import path
from django.contrib.auth import views as auth_views
from user.views import register, login_view, delete_account
from . import views
from django.conf.urls import handler403
from django.conf import settings 

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('edit/', views.profile_edit, name='profile_edit'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('delete_account/', delete_account, name='delete_account'),
]
