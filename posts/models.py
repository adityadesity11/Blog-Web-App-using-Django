from django.db import models
from datetime import datetime as dt
# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=dt.now, blank=True)
