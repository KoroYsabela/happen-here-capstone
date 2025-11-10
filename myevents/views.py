from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import HostEventForm
from events.models import Event, Booking


@login_required
def myevents_page(request):
    """
    Render the My Events page
    Handles:
        - Hosting event
        - View booked & booked past events
    """
    # Current time
    now = timezone.now()

    # Hosted Events
    hosted_events = Event.objects.filter(
        host=request.user
        ).order_by('-created_on')

    draft_events = hosted_events.filter(status=0)
    published_events = hosted_events.filter(status=1, date__gte=now)

    # Booked Events
    booked_upcoming = Booking.objects.filter(
        user=request.user,
        event__status=1,
        event__date__gte=now
    ).select_related('event').order_by('event__date')

    # Past Events
    booked_past = Booking.objects.filter(
        user=request.user,
        event__status=1,
        event__date__lt=now).select_related('event').order_by('event__date')

    # Host Event Form
    event_form = HostEventForm()

    if request.method == "POST":
        event_form = HostEventForm(request.POST, request.FILES)

        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.host = request.user

            if 'publish' in request.POST:
                event.status = 1
                messages.success(request, "Your event has been published!")
            else:
                event.status = 0
                messages.info(request, "Event saved as draft.")

            event.save()
            return redirect('myevents')
        else:
            messages.error(request,
                           "There was an error with your form."
                           "Please check your fields.")

    return render(request, 'myevents/my_events.html', {
        'draft_events': draft_events,
        'published_events': published_events,
        'event_form': event_form,
        'booked_upcoming': booked_upcoming,
        'booked_past': booked_past,
    })
