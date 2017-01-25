from django.conf.urls import url
from api.views import EventList, EventDateList, EventTimeList


urlpatterns = [
    url(r'^v1/(?P<eventdate_id>[0-9a-zA-Z_-]+)/eventtime/$', EventTimeList.as_view(), name='api-event-time-list'),
    url(r'^v1/(?P<event_id>[0-9a-zA-Z_-]+)/eventdate/$', EventDateList.as_view(), name='api-event-date-list'),
    url(r'^v1/events/$', EventList.as_view(), name='api-event-list'),
]
