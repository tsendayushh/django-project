import email
from django.db.models.query import QuerySet
from django.test import TestCase

from sports.models import Players, Sports
from sports.views import get_sports_with_multiplayers

# Create your tests here.
class SportsTests(TestCase):
    def setUp(self):
        for i in range(3):
            Players.objects.create(email=f'player{i}@test.com')

        Sports.objects.create(name="Test1")
        Sports.objects.create(name="Test2")


    def test_animals_can_speak(self):
        sport1 = Sports.objects.get(name="Test1")
        sport1.players.set = Players.objects.all()

        sport2 = Sports.objects.get(name="Test2")


        _sports = get_sports_with_multiplayers()
        self.assertTrue(isinstance(_sports, QuerySet))
