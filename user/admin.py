from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

class MyUserAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'date_of_birth',
        'is_staff',
        'is_active',
        'date_joined',
    )
    list_filter = (
        'city',  # 'location' yerine 'city' kullanıldı
        'date_of_birth',
        'is_staff',
        'is_active',
    )
    fieldsets = (
        (None, {'fields': ('username', 'email',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'address', 'country', 'city', 'zip_code', 'date_of_birth',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'phone_number', 'address', 'country', 'city', 'zip_code', 'date_of_birth', 'is_staff', 'is_active',)
        }),
    )

    
admin.site.register(MyUser, MyUserAdmin)
