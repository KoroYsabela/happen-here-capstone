from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import HostEventForm
from events.models import Event, Booking
# Unused imports removed


@login_required
def myevents_page(request):
    """
    Render the My Events page
    Handles:
        - Hosting event
        - Editing event
    """
    # Current time
    now = timezone.now()

    # Hosted Events
    hosted_events = Event.objects.filter(host=request.user).order_by('-created_on')
    draft_events = hosted_events.filter(status=0)
    published_events = hosted_events.filter(status=1, date__gte=now)

    # Booked Events
    booked_upcoming = Booking.objects.filter(user=request.user, event__status=1, event__date__gte=now).select_related('event').order_by('event__date')

    # Past Events
    booked_past = Booking.objects.filter(user=request.user, event__status=1, event__date__lt=now).select_related('event').order_by('event__date')

    # Host Event & Edit Form
    event_form = HostEventForm()
    edit_form = None

    if request.method == "POST":
        event_slug = request.POST.get("event_slug")

        # If event_slug exists → editing an event
        if event_slug:
            event = get_object_or_404(Event, slug=event_slug, host=request.user)
            edit_form = HostEventForm(request.POST, request.FILES, instance=event)

            if edit_form.is_valid():
                updated_event = edit_form.save(commit=False)

                if 'publish' in request.POST:
                    updated_event.status = 1
                    messages.success(request, "Event updated and published.")
                elif 'save_draft' in request.POST:
                    updated_event.status = 0
                    messages.info(request, "Event saved as draft.")
                else:
                    messages.success(request, "Event updated.")

                updated_event.save()
                return redirect('myevents')
            else:
                messages.error(request, "Please correct the errors in your edit form.")
        # Otherwise → hosting new event
        else:
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
                messages.error(request, "There was an error with your form. Please check your fields.")

    return render(request, 'myevents/my_events.html', {
        'draft_events': draft_events,
        'published_events': published_events,
        'event_form': event_form,
        'edit_form': edit_form or HostEventForm(),
        'booked_upcoming': booked_upcoming,
        'booked_past': booked_past,
    })


#@login_required
#def edit_event(request, slug):
#    """
#    Edit events that are both published and draft
#    """
#    event = get_object_or_404(Event, slug=slug, host=request.user)
#
#    if request.method == "POST":
#        form = HostEventForm(request.POST, request.FILES, instance=event)
#        if form.is_valid():
#            edit_event = form.save(commit=False)
#
#            # Update status depending on which button was clicked
#            if 'publish' in request.POST:
#                edit_event.status = 1
#                messages.success(
#                    request,
#                    "Your event has been published successfully!"
#                )
#            elif 'save_draft' in request.POST:
#                edit_event.status = 0
#                messages.info(request, "Your event has been saved as a draft.")
#            else:
#                messages.success(
#                    request,
#                    "Your event has been updated successfully!"
#                )
#
#            edit_event.save()
#            return redirect('myevents')
#    else:
#        form = HostEventForm(instance=event)
#
#    # Render same page again with the edit form modal visible
#    hosted_events = (
#        Event.objects.filter(host=request.user)
#        .order_by('-created_on')
#    )
#    return render(request, 'myevents/my_events.html', {
#        'hosted_events': hosted_events,
#        'edit_event_form': form,
#        'edit_event_obj': event,
#        'event_form': HostEventForm(),  # for creating new events
#    })
#