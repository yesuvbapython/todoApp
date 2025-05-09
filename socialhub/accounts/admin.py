from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import CustomChangeForm,CustomCreationForm
# Register your models here.


class cutomeAdmin(UserAdmin):
    list_display = ['email','is_active','is_admin','is_staff','is_superuser']
    model = User
    form = CustomChangeForm
    add_form = CustomCreationForm
    fieldsets = (
        ('personalinfo',{'fields':('email','username','first_name','last_name')}),
        ('permissions',{'fields':('is_active','is_admin','is_superuser','is_staff')}),
    )
    add_fieldsets =(
        (None,{
            'classes':('wide'),
            'fields':('email','username','first_name','last_name','is_admin','is_staff','is_superuser','is_active')
        })
    )

admin.site.register(User)

