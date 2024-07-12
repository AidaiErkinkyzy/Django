from django.contrib import admin
from .models import *


@admin.register(AboutUs)
class AboutUs(admin.ModelAdmin):
    list_display = ['history','why_us']


@admin.register(Employees)
class Employees(admin.ModelAdmin):
    list_display = ['image', 'employees_name', 'position']




