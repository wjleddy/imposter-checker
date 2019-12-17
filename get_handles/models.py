from django.db import models
from django.utils import timezone

class BaseHandle(models.Model):
    handle = models.CharField(max_length=15, unique_for_date="date_pulled", primary_key=True, 
                              help_text="Please do not include the @ symbol, and use only valid Twitter handle characters",
                              error_messages={'unique':'Sorry, info for that handle has already been gathered today. You can view it under "Browse Base Handles"!'})
    date_pulled = models.DateField(default=timezone.now)
    
    class Meta:
        ordering = ['handle']
        
    def __str__(self):
        return self.handle
    
class SimilarHandles(models.Model):
    base_handle_date = models.ForeignKey(BaseHandle, on_delete=models.CASCADE)
    handle = models.CharField(max_length=15)
    suspended = models.BooleanField()
    display_name = models.CharField(max_length=50, blank=True, null=True)
    number_of_tweets = models.IntegerField(blank=True, null=True)
    number_of_followers = models.IntegerField(blank=True, null=True)
    number_following = models.IntegerField(blank=True, null=True)
    date_joined = models.DateTimeField(blank=True, null=True)
    bio = models.CharField(max_length=160, blank=True, null=True)
    
    class Meta:
        ordering = ['handle']
    
    def __str__(self):
        return self.handle
