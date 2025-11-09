from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Event, Booking


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    list_display = ('title', 'date', 'location', 'host', 'status')
    search_fields = ['title', 'date', 'description']
    list_filter = ('status', 'date')
    summernote_fields = ('description',)


# Register your models here.
admin.site.register(Booking)
