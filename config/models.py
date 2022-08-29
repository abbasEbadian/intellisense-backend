from pyexpat import model
from tabnanny import verbose
from django.db import models
from solo.models import SingletonModel
# Create your models here.
class Roadmap(models.Model):
    title = models.CharField(max_length=255, help_text="e.g. Phase 1")
    sequence = models.IntegerField(help_text="sequence of this slide in slider ")
    status = models.CharField(max_length=7, choices=[
        ('done', 'Done'),
        ('ongoing', 'Ongoing'),
        ('pending', 'Pending'),
    ])
    content = models.TextField()
    

    created = models.DateTimeField(auto_now_add=True)    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return "Roadmap: " + self.title


class Util(models.Model):
    title = models.CharField(max_length=255, help_text="e.g. Decentralized perpetual multi asset platform")
    sequence = models.IntegerField(help_text="sequence in the list ")
    content = models.TextField()
    

    created = models.DateTimeField(auto_now_add=True)    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return "Util: " + self.title



class FAQ(models.Model):
    title = models.CharField(max_length=511, help_text="e.g. Decentralized perpetual multi asset platform")
    sequence = models.IntegerField(help_text="sequence in the list ")
    content = models.TextField()
    active = models.BooleanField(verbose_name="Show in website", default=True)
    created = models.DateTimeField(auto_now_add=True)    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return "FAQ: " + self.title


class CenterSlider(SingletonModel):
    first_slide_content = models.TextField(help_text="Search box will be appended to the end of this content")
    second_slide_content = models.TextField()
    third_slide_content = models.TextField()

    class Meta: 
        verbose_name = 'Centralized Slide'
        verbose_name_plural = 'Centralized Slides'


    def __str__(self) :
        return "Centeralized Slides"
