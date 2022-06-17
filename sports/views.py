from django.db.models import Count
from django.shortcuts import render
from sports.models import Sports, Players

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
    print(_queryset.query)

    return _queryset