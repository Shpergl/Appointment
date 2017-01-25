from rest_framework import serializers
from appointment.models import Event, EventTime, EventDate


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', )
        read_only_fields = ('id',)

class EventTimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventTime
        fields = ('id', 'eventTimeStart', 'eventTimeFinish',)
        read_only_fields = ('id',)
        depth = 1

class EventDateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventDate
        fields = ('id', 'eventDate',)
        read_only_fields = ('id',)
        depth = 1


