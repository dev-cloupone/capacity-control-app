from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime

class Partner(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    partnerCode = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    partnerType = models.CharField(max_length=2)
    nationalId = models.CharField(max_length=20)
    address = models.CharField(max_length=255)


