from django.contrib import admin
from django.urls import include
from django.urls import path

from config.settings import DEBUG

urlpatterns = [
    path('', include('app.urls')),
    path('', include('accounts.urls')),
]

if DEBUG:
    urlpatterns += [path('admin/', admin.site.urls)]
