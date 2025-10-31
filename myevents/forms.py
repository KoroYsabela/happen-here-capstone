from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Event


class HostEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'date', 'location',
                  'capacity', 'description', 'featured_image')
