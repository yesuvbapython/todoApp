from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import customUserChangeForm, customUserCreationForm

class customUserAdmin(UserAdmin):
    model = User
    add_form = customUserCreationForm
    form = customUserChangeForm
    list_display = ['email', 'username', 'is_admin', 'is_staff', 'is_active']

    # Explicitly defining fieldsets to avoid duplication
    fieldsets = (
        ('Personal info', {'fields': ('email', 'username', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('date_joined',)}),
    )

    # Explicitly defining add_fieldsets to avoid duplication
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff', 'is_admin'),
        }),
    )

# Register the custom admin class
admin.site.register(User, customUserAdmin)
