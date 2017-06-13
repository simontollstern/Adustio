from django.db import models
import datetime

# Create your models here.

# Creates rows in the database where blog post data will be saved
class Post(models.Model):
    # The rows, more will be added later
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=15000)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.title
