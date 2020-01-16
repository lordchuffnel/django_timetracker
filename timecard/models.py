from django.db import models
from django.contrib.auth.models import User


class Timecard(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.ForeignKey(User, related_name='timecard', on_delete=models.CASCADE, blank=False, null=False)
    start_time = models.TimeField(verbose_name="Start Time", null=False)
    lunch = models.BooleanField(default=False)
    end_time = models.TimeField(verbose_name="End Time")
    int_hours = models.DecimalField(verbose_name="Interior Hours", max_digits=4, decimal_places=1)
    ext_hours = models.DecimalField(verbose_name="Exterior Hours", max_digits=4, decimal_places=1)
    sick_day = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.username) + str(self.date) 
    
    
    