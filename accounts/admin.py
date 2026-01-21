from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "first_name", "role", "is_staff", "is_active")
    search_fields = ("email", "first_name")
    list_filter = ("role", "is_staff", "is_active")
