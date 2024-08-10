from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime

class ActivityControl(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=datetime.date.today)
    dateStart = models.TimeField()
    dateEnd = models.TimeField()
    activity = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    total = models.FloatField()


