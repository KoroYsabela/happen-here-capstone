from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

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
    featured_image = CloudinaryField('image', default='placeholder')
    created_on  = models.DateTimeField(auto_now_add=True)
    status      = models.IntegerField(choices=STATUS, default=0)
    updated_on  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.title} | hosted by {self.host}"


class Review(models.Model):
    """
    Store a review entry related to :model:`events.Event`
    """
    event       = models.ForeignKey(
                    Event, on_delete=models.CASCADE, related_name="reviews")
    author      = models.ForeignKey(
                    User, on_delete=models.CASCADE, related_name="reviewer")
    rating      = models.PositiveIntegerField(
                    validators=[MaxValueValidator(5), MinValueValidator(1)])
    body        = models.TextField()
    created_on  = models.DateTimeField(auto_now_add=True)
    updated_on  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["rating"]

    def __str__(self):
        return f"{self.event} - reviewed by {self.author}"


class Booking(models.Model):
    """
    Store a event booking related to :model:`events.Event`
    """
    user      = models.ForeignKey(
                    User, on_delete=models.CASCADE, related_name="event_booker")
    event       = models.ForeignKey(
                    Event, on_delete=models.CASCADE, related_name="event_bookings")
    booked_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["booked_at"]

    def __str__(self):
        return f"{self.event} booked by {self.user}"
