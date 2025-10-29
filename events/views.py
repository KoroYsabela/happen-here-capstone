from django.shortcuts import render
from django.views import generic
from .models import Event
#from django.http import HttpResponse

# Create your views here.

#def home_page_view(request):
#    return HttpResponse("Hello, world!")

class EventList(generic.ListView):
    #model = Event
    queryset = Event.objects.all()
    template_name = "events/index.html"
