from statistics import mode
from django.db import models
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField

User = get_user_model()

class Manager(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE,related_name='manager_id')
    total_invest = models.IntegerField()
    AUM = models.IntegerField(help_text="in percent")
    returns = models.IntegerField(help_text="in percent")
    investers = models.IntegerField(help_text="in percent ")

    corresponding_page = MultiSelectField(max_length=255, max_choices=5, choices=[
        ('all', 'All'),
        ('forex', 'Forex'),
        ('stocks', 'Stocks'),
        ('commodities', 'Commodities'),
        ('indices', 'Indices'),
        ('etf', 'ETF'),
        ('crypto', 'Crypto'),
    ], default='all')


    created = models.DateTimeField(auto_now_add=True)    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return "Manager: " + self.user_id.first_name
