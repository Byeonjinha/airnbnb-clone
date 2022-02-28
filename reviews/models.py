from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):
    """ Review Model Definition"""
    review = models.TextField()
    accuracy = models.TextField()
    communication = models.TextField()
    cleanLiness = models.TextField()
    location = models.TextField()
    check_in = models.TextField()
    value = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)
# Create your models here.
