from django.db import models


class UserRideEntry(models.Model):
    """
    A class used to store ride information for any rides that this user has
    taken or created
    """

    ride_id = models.CharField()
    owner = models.CharField()
    purpose = models.CharField()
    spoint = models.CharField()
    destination = models.CharField()
    type = models.CharField()
    date = models.CharField()
    hour = models.CharField()
    minute = models.CharField()
    ampm = models.CharField()
    max_size = models.CharField()
    details = models.CharField()

