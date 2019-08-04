from django.contrib import admin

# Register your models here.
from .models import Region

# Register your models here.

class RegionAdmin(admin.ModelAdmin):
    list_display = ['code', 'name_region', 'get_town']

    def get_town (self, obj):
        string = ''
        for town in obj.town.all():
            string += f'Código: {town.code} - Nombre: {town.name_town} || '
        return string 

admin.site.register(Region, RegionAdmin) 