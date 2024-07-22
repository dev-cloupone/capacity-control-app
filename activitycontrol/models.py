from django.db import models
import uuid
class ActivityControl(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    dateStart = models.FloatField()
    dateEnd = models.FloatField()
    activity = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    total = models.FloatField()

