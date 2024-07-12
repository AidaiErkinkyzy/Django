from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "image")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "category", "image", "gram")
