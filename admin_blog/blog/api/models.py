from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=40)
    content = models.TextField()
    creation_date = models.DateField(auto_now=True)
    publish_date = models.DateField(auto_now=True)
