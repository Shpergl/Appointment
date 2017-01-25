import simplejson

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from appointment.forms import EventForm, AddDayForm, ParticipateForm
from appointment.models import Event, EventTime, EventDate, Participants


def appointent_list(request):
    events = Event.objects.all()
    context = {
        "events": events,
    }
    return render(request, 'appointment/events.html', context)

@csrf_exempt
def get_event_time(request, id):
    eventDate = EventDate.objects.get(id=id)
    eventTime = EventTime.objects.filter(eventDate=eventDate)
    time_dict = {}
    for time in eventTime:
        time_dict[time.id] = time.__str__()
    return HttpResponse(simplejson.dumps(time_dict))

@csrf_exempt
def get_event_part(request, id):
    participants = Participants.objects.filter(eventTime=id)
    part_dict = {}
    for part in participants:
        part_dict[part.name] = part.email
    return HttpResponse(simplejson.dumps(part_dict))

def appointment_detail(request, id):
    event = get_object_or_404(Event, id=id)
    form = ParticipateForm(event=event.id)
    context = {
        "event" : event,
        "form": form,
    }
    return render(request, 'appointment/eventDetail.html', context)

@transaction.atomic
def add_participant (request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        form = ParticipateForm(request.POST, event=event.id)
        if form.is_valid():
            eventDate = form.cleaned_data['eventDate']
            eventTime = form.cleaned_data['eventTime']
            if request.user.is_authenticated:
                name = request.user.username
                email = request.user.email
            else:
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
            participant = Participants(eventTime=eventTime, name=name, email=email)
            participant.save()

            part = Participants.objects.filter(eventTime=eventTime)
            context = {
                "form" : form,
                "event" : event,
                "part" : part,
            }
            return render(request, 'appointment/eventDetail.html', context)
        else:

            context = {"form" : form,
                       "event" : event,
                       }
            return render(request, 'appointment/eventDetail.html', context)

@login_required
@transaction.atomic
def add_event (request):
    form = EventForm()
    context = {
        "form": form,
    }
    return render(request, 'appointment/eventForm.html', context)

@login_required
@transaction.atomic
def save_event (request):
    if request.method == 'POST':
        form = EventForm(request.POST, instance=request.user)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            starter = request.user

            event = Event(title=title, description=description, starter=starter)
            event.save()
            return redirect('event-detail', event.id)
        else:
            form = EventForm()
            context = {"form" : form}
            return render(request, 'appointment/eventForm.html', context)

@login_required
@transaction.atomic
def event_add_day(request, id):
    event = get_object_or_404(Event, id=id)
    form = AddDayForm()
    context = {
        "form": form,
        "event": event,
    }
    return render(request, 'appointment/eventAddDay.html', context)

@login_required
@transaction.atomic
def event_save_day(request, id):
    if request.method == 'POST':
        form = AddDayForm(request.POST, instance=request.user)
        event = get_object_or_404(Event, id=id)

        if form.is_valid():
            eventDate = form.cleaned_data['eventDate']
            eventTimeStart = form.cleaned_data['eventTimeStart']
            eventTimeFinish = form.cleaned_data['eventTimeFinish']

            try:
                eventDateInst=EventDate.objects.get(event=event, eventDate=eventDate)
            except:
                eventDateInst = EventDate(eventDate=eventDate, event=event)
                eventDateInst.save()
            finally:
                eventTimeInst = EventTime(eventTimeStart = eventTimeStart,
                                          eventTimeFinish=eventTimeFinish, eventDate=eventDateInst)
                eventTimeInst.save()
            return redirect('event-detail', event.id)
        else:
            return redirect('event-add-day', event.id)
