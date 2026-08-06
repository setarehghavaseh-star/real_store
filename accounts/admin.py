from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User




@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display=('phone_number','first_name','last_name','is_staff')
    ordering = ('phone_number',)