
from django.contrib import admin
from django.urls import path, include
from register import views as v

from .connector import send_message, make_as_read

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('django.contrib.auth.urls')),
    path('', include('lab.urls')),
    path('register/',v.register, name='register'),
    path('ajax/send-message/', send_message, name='send_message'),
    path('ajax/make-as-read/', make_as_read, name='make_as_read')
]
