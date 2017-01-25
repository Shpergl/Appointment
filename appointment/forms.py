import models
from django import forms
from django.forms import SelectDateWidget
from appointment.models import Event, EventTime, Participants, EventDate
from crispy_forms.helper import FormHelper


class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    class Meta():
        model = Event
        fields = ('title', 'description',)

class ParticipateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        event = kwargs.pop('event', None)
        self.helper = FormHelper()
        super(ParticipateForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        if event:
            self.fields['eventDate']=forms.ModelChoiceField(queryset=EventDate.objects.filter(event=event),
                                                            widget = forms.RadioSelect())
            self.fields['eventTime'] = forms.ModelChoiceField(queryset=EventTime.objects.filter(eventDate=EventDate.objects.filter(event=event)),
                                                             widget=forms.RadioSelect())
    class Meta():
        model = Participants
        fields=('name', 'email')

class EventDateForm(forms.ModelForm):
    class Meta():
        model = EventDate
        fields = ('eventDate', )

    def __init__(self, event, *args, **kwargs):
        super(EventDateForm, self).__init__(*args, **kwargs)
        self.fields['eventDate'].queryset = EventDate.objects.filter(event=event)
        self.files['eventDate'].widget = forms.RadioSelect()

class EventTimeForm(forms.ModelForm):
    class Meta():
        model = EventTime
        fields = ('eventTimeStart',)

class ParticipantForm(forms.Form):
    class Meta():
        model = Participants
        fields = ('name', 'email')

class AddDayForm(forms.ModelForm):
    class Meta():
        model = EventTime
        fields = ('eventTimeStart', 'eventTimeFinish')
    eventDate = forms.DateField(widget=SelectDateWidget)
