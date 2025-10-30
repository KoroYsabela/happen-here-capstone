from django.views import generic
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
