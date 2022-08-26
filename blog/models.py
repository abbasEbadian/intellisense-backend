
from tkinter.tix import Tree
from django.db import models
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from random import randint
from multiselectfield import MultiSelectField

class BlogCategory(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.title


        
class Blog(models.Model):
    category_id = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, verbose_name="Category", null=True, blank=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(verbose_name="main image", upload_to="blogs/"+str(randint(0, 99999999999999))+"/", null=True, blank=True)
    image_alt = models.CharField(verbose_name="image alt", max_length=255, null=True, blank=True)
    summary = models.TextField()
    content = models.TextField(verbose_name='content')
    estimeted_read_time = models.PositiveIntegerField(verbose_name="Estimeted Read Time( in minutes )", default=2)
    
    corresponding_page = MultiSelectField(max_length=255, max_choices=5, choices=[
        ('all', 'All'),
        ('forex', 'Forex'),
        ('stocks', 'Stocks'),
        ('commodities', 'Commodities'),
        ('indices', 'Indices'),
        ('etf', 'ETF'),
        ('crypto', 'Crypto'),
    ], default='all')

    # reviews = models.IntegerField(verbose_name="تعداد بازدید", default=0)
    # show_in_sitemap =models.BooleanField(verbose_name="نمایش در سایت مپ", default=True)
    # meta_title = models.CharField(verbose_name="تایتل", max_length=255, blank=True, null=True)
    # meta_description = models.TextField(verbose_name="متا دسکریپشن", blank=True, null=True)
    # meta_keywords = models.TextField(verbose_name="متا کیوردز", blank=True, null=True)
    # meta_canonical = models.TextField(verbose_name="کنونیکال", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.title
