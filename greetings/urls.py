from django.urls import include, path

from greetings.views import get_greetings

import json


urlpatterns = [
    path('test_view/', get_greetings, name="greetings"),
]