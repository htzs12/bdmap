from django.contrib import admin
from .models import address_info


class AddressAdmin(admin.ModelAdmin):
    list_display = ['longitude','latitude','data']


admin.site.register(address_info,AddressAdmin)