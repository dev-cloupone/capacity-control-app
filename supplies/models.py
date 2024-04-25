from django.db import models
import uuid
class Supplie(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=100)
    field_size = models.FloatField()
    quantity_per_hectare = models.FloatField()
    value = models.FloatField()
    total = models.FloatField()
