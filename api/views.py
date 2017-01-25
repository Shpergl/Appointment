from rest_framework import generics
from rest_framework.permissions import AllowAny
from appointment.models import Event, EventDate, EventTime
from serializer import EventSerializer, EventDateSerializer, EventTimeSerializer


class EventList(generics.ListAPIView):
    """
    /api/v1/event/ [GET]-Return list of all events.
    """
    model = Event
    serializer_class = EventSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Event.objects.all()

class EventDateList(generics.ListAPIView):
    """
    /api/v1/<event_id>/eventdate/ [GET]-Return list of all possible dates for event.
    """
    model = EventDate
    serializer_class = EventDateSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        eventId = self.kwargs['event_id']
        return EventDate.objects.filter(event=eventId)

class EventTimeList(generics.ListAPIView):
    """
    /api/v1/<eventdate_id>/eventtime/ [GET]- Return list of all possible time ranges for date
    """
    model = EventTime
    serializer_class = EventTimeSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        eventdateId = self.kwargs['eventdate_id']
        return EventTime.objects.filter(eventDate=eventdateId)
