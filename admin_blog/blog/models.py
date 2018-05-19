import datetime
from django.db import models


class Posts(models.Model):

    DEVELOPER = 'developer'
    DEVOPS = 'devops'
    AUTOMATION = 'automation'

    CATEGORY_CHOICES = (
        (DEVELOPER, 'Developer'),
        (DEVOPS, 'DevOps'),
        (AUTOMATION, 'Developer')
    )

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=40)
    content = models.CharField(max_length=500)
    creation_date = models.DateField()
    publish_date = models.DateField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
