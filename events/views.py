from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Event, Booking
from myevents.forms import HostEventForm


# Create your views here.


class EventList(generic.ListView):
    # Current time
    now = timezone.now()

    model = Event
    template_name = "events/index.html"
    context_object_name = 'event_list'

    def get_queryset(self):
        """Return published events ordered by date."""
        return (
            Event.objects.filter(status=1, date__gte=self.now)
            .order_by("date")
        )


class AllEventsList(generic.ListView):
    # Current time
    now = timezone.now()

    queryset = Event.objects.filter(status=1, date__gte=now).order_by('date')
    template_name = "events/all_events.html"
    paginate_by = 6


def event_detail(request, slug):
    """
    Display the event details in its own page
    """
    # Current time
    now = timezone.now()

    event = get_object_or_404(Event, slug=slug)

    # Define
    user_booking = None

    # Provide an edit form instance (pre-filled)
    # Only hosts should be able to submit edits, but providing the form
    # in the template avoids template errors. The modal will only be shown
    # when routed through the `edit_event` view
    if request.user.is_authenticated:
        # Check if player has already booked the event
        # only when logged in otherwise causes an error
        user_booking = Booking.objects.filter(user=request.user, event=event).first()

        edit_form = HostEventForm(instance=event)
    else:
        edit_form = HostEventForm()

    return render(
        request,
        "events/event_detail.html",
        {
            "event": event,
            "edit_form": edit_form,
            "user_booking": user_booking,
            "now": now,
        },
    )


@login_required
def edit_event(request, slug):
    """
    In the event detail page:
        - Show modal which includes edit form for the event
    """
    event = get_object_or_404(Event, slug=slug, host=request.user)

    if request.method == 'POST':

        form = HostEventForm(request.POST, request.FILES, instance=event)

        if form.is_valid():

            updated = form.save(commit=False)

            if 'publish' in request.POST:
                updated.status = 1
            elif 'save_draft' in request.POST:
                # Prevent published event from being turned back into a draft
                # Can cause errors with users that have bookings to the event
                if event.status == 1:
                    messages.warning(
                        request, "Published events cannot be reverted."
                    )
                else:
                    updated.status = 0
                    messages.info(request, "Event saved as draft.")

            updated.save()
            messages.success(request, "Event updated.")
            return redirect('event_detail', slug=event.slug)
        else:
            # Fall through to re-render page with modal and errors
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = HostEventForm(instance=event)

    return render(
        request,
        'events/event_detail.html',
        {'event': event,
         'edit_form': form,
         'show_edit_modal': True},
    )


@login_required
def book_event(request, slug):
    """
    Make a booking for an event
    """
    event = get_object_or_404(Event, slug=slug)

    if request.method == "POST":
        # Prevent overbooking
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


@login_required
def cancel_event(request, slug, booking_id):
    """
    Allow the user that has booked a space in the event to cancel.
    Increases event capacity again by 1.

    Use booking id to get the booking for the slug
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    event = booking.event

    if request.method == "POST":
        # Delete booking
        booking.delete()

        # Increase event capacity by 1
        event.capacity += 1
        event.save(update_fields=["capacity"])
        
    messages.success(request, f"Your booking for '{event.title}' has been cancelled.")
    return redirect('event_detail', slug=event.slug)


@login_required
def delete_event(request, slug):
    """
    Delete a published event that is hosted by the user
    """
    event = get_object_or_404(Event, slug=slug, host=request.user)

    if request.method == "POST":
        event.delete()
        messages.success(request, f"Your event '{event.title}' has been deleted.")
        return redirect("myevents")
