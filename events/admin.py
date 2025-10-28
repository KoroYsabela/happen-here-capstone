from django.contrib import admin
from .models import Event, Review, Booking


# Register your models here.
admin.site.register(Event)
admin.site.register(Review)
admin.site.register(Booking)

