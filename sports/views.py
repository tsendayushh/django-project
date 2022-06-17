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

    
    # A raw query for selecting the sports that multiple (= more than or equal to 2) players are associated with
    """
    SELECT `sports`.`id`, `sports`.`name`, COUNT(`sports_players`.`players_id`) AS `player_count` 
    FROM `sports` 
    LEFT OUTER JOIN `sports_players` 
    ON (`sports`.`id` = `sports_players`.`sports_id`) 
    GROUP BY `sports`.`id` 
    HAVING COUNT(`sports_players`.`players_id`) >= 2 
    ORDER BY NULL
    """
    print(_queryset)

    # printing raw query of the above queryset
    # print('multiplayers sports query:',_queryset.query)

    return _queryset


def get_sports_with_no_player():
    # This function retrieves sports that no player is associated with
    """
    param: None
    returns: queryset
    """
    _queryset = Sports.objects.annotate(player_count=Count('players')).filter(player_count=0)

    # A raw query for selecting the sports that no player is associated with
    """
    SELECT `sports`.`id`, `sports`.`name`, COUNT(`sports_players`.`players_id`) AS `player_count` 
    FROM `sports` 
    LEFT OUTER JOIN `sports_players` ON 
    (`sports`.`id` = `sports_players`.`sports_id`) 
    GROUP BY `sports`.`id` 
    HAVING COUNT(`sports_players`.`players_id`) = 0 
    ORDER BY NULL
    """
    print(_queryset)

    # printing raw query of the above queryset
    # print('sports with no players query:',_queryset.query)

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
