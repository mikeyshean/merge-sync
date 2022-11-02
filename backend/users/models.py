from django.db import models
from django.contrib.auth.models import AbstractUser
from backend.core.models import TimestampedModel

class User(AbstractUser, TimestampedModel):
    company = models.ForeignKey("companies.Company", on_delete=models.PROTECT, null=True, blank=True)
