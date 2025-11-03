from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import HostEventForm
from events.models import Event


@login_required
def myevents_page(request):
    """
    Render the My Events page
    """
    hosted_events = Event.objects.filter(host=request.user).order_by('-created_on')

    draft_events = hosted_events.filter(status='0')
    published_events = hosted_events.filter(status=1)

    if request.method == "POST":
        # Include request.FILES to handle file uploads from the form
        event_form = HostEventForm(request.POST, request.FILES)

        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.host = request.user

            # if draft or published
            if 'publish' in request.POST:
                event.status = 1
                messages.success(request, "Your event has been published!")
            else:
                event.status = 0
                messages.info(request, "Your event has been saved as a draft.")

            event.save()
            return redirect('myevents')
        else:
            messages.error(request, "There was an error with your form. " \
            "Please check you have filled in the fields correctly.")
    else:
        event_form = HostEventForm

    return render(
        request,
        'myevents/my_events.html',
        {'draft_events': draft_events,
         'published_events': published_events,
         'event_form': event_form,
         })


#@login_required
#def host_event(request):
#    """
#    Host an event
#    """
#    if request.method == "POST":
#        # Include request.FILES to handle file uploads from the form
#        event_form = HostEventForm(request.POST, request.FILES)
#
#        if event_form.is_valid():
#            event = event_form.save(commit=False)
#            event.host = request.user
#
#            # if draft or published
#            if 'publish' in request.POST:
#                event.status = 1
#                messages.success(request, "Your event has been published!")
#            else:
#                event.status = 0
#                messages.info(request, "Your event has been saved as a draft.")
#
#            event.save()
#            return redirect('myevents')
#
#        # Invalid form — show errors
#        return render(request, 'myevents/my_events.html', {'event_form': event_form})
#
#    #  Add this for GET requests
#    event_form = HostEventForm()
#    return render(request, 'myevents/my_events.html', {'event_form': event_form})
