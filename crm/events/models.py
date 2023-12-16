from django.db import models

# Create your models here.

class EventType(models.Model):
    
    name = models.CharField(max_length=255)


class DevEvent(models.Model):

    name = models.CharField(255)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    event_type = models.OneToOneField(EventType, on_delete=models.CASCADE)
    users = models.ManyToManyField("auth.User")
