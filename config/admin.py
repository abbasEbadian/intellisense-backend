from django.contrib import admin
from .models import Roadmap, Util
# Register your models here.

@admin.register(Roadmap)
class SomeModelAdmin(admin.ModelAdmin):  # instead of ModelAdmin
    list_display = ['id', 'title', 'sequence', 'content', 'status']

@admin.register(Util)
class UtilAdmin(admin.ModelAdmin):  # instead of ModelAdmin
    list_display = ['id', 'title', 'sequence', 'content']