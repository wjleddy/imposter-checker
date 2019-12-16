from django.db import models
from django.utils import timezone

class BaseHandle(models.Model):
    handle = models.CharField(max_length=15, unique_for_date="date_pulled", primary_key=True, 
                              help_text="Please do not include the @ symbol, and use only valid Twitter handle characters")
    date_pulled = models.DateField(default=timezone.now)
    
    class Meta:
        ordering = ['handle']
        
    def __str__(self):
        return self.base_handle
    
class SimilarHandles(models.Model):
    base_handle_date = models.ForeignKey(BaseHandle, on_delete=models.CASCADE)
    handle = models.CharField(max_length=15)
    suspended = models.BooleanField()
    display_name = models.CharField(max_length=50)
    number_of_tweets = models.IntegerField()
    number_of_followers = models.IntegerField()
    number_following = models.IntegerField()
    marked_parody = models.BooleanField()
    date_joined = models.DateTimeField()
    bio = models.CharField(max_length=160)
    
    class Meta:
        ordering = ['handle']
    
    def __str__(self):
        return self.handle
