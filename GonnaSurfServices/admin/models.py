import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GonnaSurfServices.settings")

from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=200, unique=True)
    parent = models.BigIntegerField(blank=True, null=True)
    path = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return 'place_name: ' + self.name + ' parent: ' + str(self.parent)

    @classmethod
    def create(cls, name, parent):
        place = cls(name=name, parent=parent)
        return place


class Spot(models.Model):
    spot_name = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()
    place = models.ForeignKey(Place)

    def __unicode__(self):
        return str(self.spot_name)

    def __str__(self):
        return self.spot_name

#class GoogleGeoCoding(models.Model):
#    spot = models.ForeignKey(Spot)
#    status = models.CharField(max_length=10)
#    partial_match = models.BooleanField
#    location_type = models.CharField(max_length=10)
#    lat = models.FloatField
#    lng = models.FloatField

class MagicSeaWeedLink(models.Model):
    link = models.CharField(max_length=200)
    entity_type = models.CharField(max_length=200)
    entity_id = models.BigIntegerField()
    entity_str = models.CharField(max_length=200)
