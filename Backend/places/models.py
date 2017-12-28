from django.db import models

from cities.models import City


class Place(models.Model):
    """ """
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s - %s' % (self.name, self.city.name, self.city.state.name)