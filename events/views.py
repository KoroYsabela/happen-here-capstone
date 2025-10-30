from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Event


# Create your views here.


class EventList(generic.ListView):
    # Use model + get_queryset to avoid evaluating querysets at import time
    model = Event
    template_name = "events/index.html"
    # make the template context variable explicit
    # default would be event_list
    context_object_name = 'event_list'

    def get_queryset(self):
        """Return published events ordered by date."""
        return Event.objects.filter(status=1).order_by('date')


#class EventDetail(generic.DetailView):
#    model = Event
#    template_name = 'events/event_detail.html'
#    context_object_name = 'event_detail'


def event_detail(request, slug):
    queryset = Event.objects.filter(status=1)
    event = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "events/event_detail.html",
        {"event": event},
    )
