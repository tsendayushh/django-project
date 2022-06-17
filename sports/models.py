from django.db import models

CHAR_MAX_LENGTH = 50
# Create your models here.

class Players(models.Model):
    email = models.EmailField(verbose_name="Email",unique=True, null=False)

    class Meta:
        db_table = "players"
        verbose_name = "players"
        verbose_name_plural = "Players"

        
class Sports(models.Model):
    name = models.CharField(verbose_name="Email",unique=True, null=False, max_length=CHAR_MAX_LENGTH, default="Baseball")
    players = models.ManyToManyField(Players)

    class Meta:
        db_table = "sports"
        verbose_name = "sports"
        verbose_name_plural = "Sports"