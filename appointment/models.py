from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


SHORT_TEXT_LEN = 100

class Event(models.Model):
    title = models.CharField(verbose_name="Title", max_length=200)
    description = models.TextField(verbose_name='Description')
    starter = models.ForeignKey(User, verbose_name="Event Author")

    def __str__(self):
        return self.title

    def get_cut(self):
        if self.description > SHORT_TEXT_LEN:
            return self.description[:SHORT_TEXT_LEN]
        return self.description

class EventDate(models.Model):
    eventDate = models.DateField(verbose_name="Event Date")
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.eventDate.strftime('%d %B %Y'))

class EventTime(models.Model):
    eventTimeStart = models.TimeField(verbose_name='Event Start Time')
    eventTimeFinish = models.TimeField(verbose_name='Event Finish Time')
    eventDate = models.ForeignKey(EventDate, verbose_name="Event Date", on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.eventTimeStart.strftime('%M:%H'), self.eventTimeFinish.strftime('%M:%H'))

class Participants (models.Model):
    name = models.CharField(verbose_name='Full Name', max_length=200)
    email = models.EmailField(verbose_name='Email', max_length=100)
    eventTime = models.ForeignKey(EventTime, null=True, on_delete=models.CASCADE)
