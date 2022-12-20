from django.db import models
from django.contrib.postgres.fields import ArrayField


class Player(models.Model):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    rookie = models.IntegerField()
    retirement = models.IntegerField(null=True, blank=True)
    club = models.CharField(max_length=255)
    position = models.CharField(max_length=50, blank=True, null=True)
    world_cup = models.IntegerField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    image1 = models.CharField(max_length=255, blank=True, null=True)
    image2 = models.CharField(max_length=255, blank=True, null=True)
    image3 = models.CharField(max_length=255, blank=True, null=True)
    image4 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nickname