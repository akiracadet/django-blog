from django.contrib import admin
from django.urls import include
from django.urls import path

from config.settings import DEBUG

urlpatterns = [

]

if DEBUG:
    urlpatterns += [path('admin/', admin.site.urls)]
