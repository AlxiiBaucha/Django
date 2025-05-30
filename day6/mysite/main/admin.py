from django.contrib import admin
from .models import *

admin.site.register(Project)
class Projectadmin(admin.ModelAdmin):
    list_display = ('title', 'start_date')
    list_filter = ('start_date')
    search_fields = ('title', 'description')
    ordering = ('-start_date',)
