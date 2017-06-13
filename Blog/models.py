from django.db import models

import datetime
# Create your models here.

# Creates rows in the database where blog post data will be saved
class BlogPosts(models.Model):
    # The rows, more will be added later
    post_title = models.CharField(max_length=150)
    post_text = models.CharField(max_length=15000)
    # post_pub_date = datetime.now()
    def __str__(self):
        return self.post_title
