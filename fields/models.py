from django.db import models
import uuid
class Field(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    name = models.CharField(max_length=100)
    size = models.FloatField()
