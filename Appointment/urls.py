from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/', auth_views.login, {'template_name': 'appointment/login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^appointment/', include('appointment.urls')),
    url(r'^api/', include('api.urls')),
]
