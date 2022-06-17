from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from sports.models import Sports, Players
# from sports.serializers import GetSportsSerializer

# Create your views here.
def get_sports_with_multiplayers(count=2):
    # This function retrieves sports that multi players are associated with
    """
    param: None
    returns: queryset
    """
    _queryset = Sports.objects.annotate(player_count=Count('players')).filter(player_count__gte=2)
    print(_queryset)

    # printing raw query of the above queryset
    print('multiplayers sports query:',_queryset.query)

    return _queryset


def get_sports_with_no_player():
    # This function retrieves sports that no player is associated with
    """
    param: None
    returns: queryset
    """
    _queryset = Sports.objects.annotate(player_count=Count('players')).filter(player_count=0)
    print(_queryset)

    # printing raw query of the above queryset
    print('sports with no players query:',_queryset.query)

    return _queryset


class GetSportsSerializer(ModelSerializer):
    class Meta:
        model = Sports
        fields = [
            "name",
            # "players"
        ]

class GetSportsView(ModelViewSet):
    """
    A view for retrieving Sports 
    """
    queryset = Sports.objects.all()
    serializer_class = GetSportsSerializer
    http_method_names = ["get"]

    def get_queryset(self):
        queryset = super(GetSportsView, self).get_queryset()
        return queryset.order_by("name")

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # print("queryset", queryset)
        if queryset and queryset.exists():
            _list = []
            for _sport in queryset:
                serializer = GetSportsSerializer(_sport)
                _players = [ele.email for ele in _sport.players.all()]
                _list.append({**serializer.data, 'players':_players})
            return HttpResponse(_list)
        return HttpResponse("No datas")
