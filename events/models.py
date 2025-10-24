from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Event(models.Model):
    """
    Store a single event created by hose (user)
    """
    title       = models.CharField(max_length=100, unique=True)
    slug        = models.CharField(unique=True, blank=True)
    date        = models.DateTimeField()
    location    = models.CharField(max_length=150)
    host        =  models.ForeignKey(
                    User, on_delete=models.CASCADE, related_name="hosted_events")
    description = models.TextField(blank=True)
    capacity    = models.PositiveIntegerField()
    #image placeholder
    created_on  = models.DateTimeField(auto_now_add=True)
    updated_on  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.title} | hosted by {self.host}"
