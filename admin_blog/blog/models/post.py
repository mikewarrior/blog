from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=40)
    content = models.CharField(max_length=500)
    creation_date = models.DateField(auto_now=True)
    publish_date = models.DateField(auto_now=True)
