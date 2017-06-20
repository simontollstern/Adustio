from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

# Creates rows in the database where blog post data will be saved
class Post(models.Model):
    # The rows, more will be added later
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=15000)
    youtube = models.CharField(max_length=150, default='', blank=True)
    soundcloud = models.CharField(max_length=150, default='', blank=True)
    date = models.DateTimeField(default=timezone.now())
    pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title
