from django.db import models

from states.models import State


class City(models.Model):
    """ """
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return '%s - %s - %s' % (self.name, self.state.name, self.state.country.name)
