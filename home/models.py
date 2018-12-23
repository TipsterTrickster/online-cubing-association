from django.db import models


class Recent(models.Model):
    name = models.CharField(max_length=1000, default='')
    title = models.CharField(max_length=1000, default='')
    details = models.CharField(max_length=100000, default='')

