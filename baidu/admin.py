from django.contrib import admin
from .models import address_info


class AddressAdmin(admin.ModelAdmin):
    list_display = ['id','longitude','latitude','address','phone','desc','video']


admin.site.register(address_info,AddressAdmin)