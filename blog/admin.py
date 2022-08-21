from django_summernote.admin import SummernoteModelAdmin
from .models import Blog, BlogCategory
from django.contrib import admin

# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ['content', 'summary']
    list_display = ("title", "category_id" , "created")

admin.site.register(Blog, SomeModelAdmin)
admin.site.register(BlogCategory)