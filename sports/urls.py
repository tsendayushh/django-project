from django.urls import path
from sports.views import GetSportsView


urlpatterns = [
    path("get_sports/", GetSportsView.as_view({"get": "list"})),
]
