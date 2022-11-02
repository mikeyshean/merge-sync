from django.db import models
from backend.core.models import TimestampedModel

class Company(TimestampedModel):
    id: int
    name = models.CharField(max_length=200, help_text="Name of the company", db_index=True)
