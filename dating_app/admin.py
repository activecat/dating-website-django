from django.contrib import admin

from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender')
    ordering = ['user']


admin.site.register(Profile, ProfileAdmin)
