from django.contrib import admin
from .models import Town

# Register your models here.

class TownAdmin(admin.ModelAdmin):
    list_display = ['code', 'name_town', 'status']

admin.site.register(Town, TownAdmin) 