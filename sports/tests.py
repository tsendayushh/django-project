import email
from django.db.models.query import QuerySet
from django.test import TestCase

from sports.models import Players, Sports
from sports.views import get_sports_with_multiplayers, get_sports_with_no_player

# Create your tests here.
class SportsTests(TestCase):
    def setUp(self):
        for i in range(3):
            Players.objects.create(email=f'player{i}@test.com')

        sport1 = Sports.objects.create(name="Test1")
        sport1.players.set = Players.objects.all()
        # sport1.save()
        sport2 = Sports.objects.create(name="Test2")
        # sport2.save()


    def test_multiplayer_sport_retriever(self):
        _sports = get_sports_with_multiplayers()
        self.assertTrue(isinstance(_sports, QuerySet))

    def test_noplayer_sport_retriever(self):
        _sports = get_sports_with_no_player()
        self.assertTrue(isinstance(_sports, QuerySet))