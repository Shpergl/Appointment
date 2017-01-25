from django.conf.urls import url
from appointment import views

urlpatterns = [
    url(r'^list/$', views.appointent_list, name='event-list'),
    url(r'^(?P<id>[0-9]+)/$', views.appointment_detail, name='event-detail'),
    url(r'^get_event_time/(?P<id>[0-9]+)/$', views.get_event_time, name='get-event-time'),
    url(r'^get_event_part/(?P<id>[0-9]+)/$', views.get_event_part, name='get-event-part'),
    url(r'^addEvent/$', views.add_event, name='event-add'),
    url(r'^saveEvent/$', views.save_event, name='event-save'),
    url(r'^addDayEvent/(?P<id>[0-9]+)/$', views.event_add_day, name='event-add-day'),
    url(r'^saveDayEvent/(?P<id>[0-9]+)/$', views.event_save_day, name='event-save-day'),
    url(r'^addParticipant/(?P<id>[0-9]+)/$', views.add_participant, name='add-participant'),
]