from django.contrib import admin
from .models import Phone

# Register your models here.

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    """Phone"""
    list_display = ("name", "phonenumber", "city", "adress", "email")
