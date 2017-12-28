from django.db import models

from countries.models import Country


class State(models.Model):
    """ """
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.name, self.country.name)