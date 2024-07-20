from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone", "message", "created_at")






