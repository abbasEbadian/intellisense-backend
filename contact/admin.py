from django.contrib import admin
from .models import Contact
# Register your models here.
@admin.register(Contact)
class SomeModelAdmin(admin.ModelAdmin):  # instead of ModelAdmin
    list_display = ['id', 'name','email', 'subject', 'content']