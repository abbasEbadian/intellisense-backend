from django.db import models

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