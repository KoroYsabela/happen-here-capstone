from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Event, Booking


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

@login_required
def book_event(request, slug):
    """
    Make a booking for an event
    """
    event = get_object_or_404(Event, slug=slug)

    if request.method == "POST":
        # Check if there is still space incase of overbooking)
        if event.capacity <= 0:
            messages.error(request, "Sorry, this event is fully booked.")
            return redirect('event_detail', slug=event.slug)
        
        # Check if user has already booked this event
        if Booking.objects.filter(event=event, user=request.user).exists():
            messages.info(request, "You already booked this event.")
            return redirect('event_detail', slug=event.slug)

        # Create booking
        Booking.objects.create(user=request.user, event=event)

        # Decrease capacity by 1
        event.capacity -= 1
        event.save()

    messages.success(request, "Your booking was successful!")
    return HttpResponseRedirect(reverse('event_detail', args=[slug]))

