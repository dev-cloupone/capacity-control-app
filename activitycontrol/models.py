from django.db import models
import uuid
import datetime

class ActivityControl(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    # userId = models.UUIDField(
    #     primary_key = False,
    #     editable = False
    # )
    date = models.DateField(default=datetime.date.today)
    dateStart = models.TimeField()
    dateEnd = models.TimeField()
    activity = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    total = models.FloatField()

