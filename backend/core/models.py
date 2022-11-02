from django.db import models
from django.utils import timezone

# Create your models here.
class TimestampedModel(models.Model):

    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
