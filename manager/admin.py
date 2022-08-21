from django.contrib import admin
from .models import Manager
# Register your models here.
@admin.register(Manager)
class SomeModelAdmin(admin.ModelAdmin):  # instead of ModelAdmin
    list_display = ['id']