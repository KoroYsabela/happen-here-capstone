from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
from events.models import Event


class HostEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'date', 'location',
                  'capacity', 'description', 'featured_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(
                attrs={'class': 'form-control', 'min': 1}
            ),
            'description': SummernoteWidget(),
            'featured_image': forms.ClearableFileInput(
                attrs={'class': 'form-control'}
            ),
        }
