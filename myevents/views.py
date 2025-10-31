from django.shortcuts import render
from django.views import generic
from events.models import Event, Booking


# Create your views here.

#class MyEventsPage(generic.TemplateView):
#    template_name = "myevents/my_events.html"

def myevents_page(request):
    return render(request, 'myevents/my_events.html')
