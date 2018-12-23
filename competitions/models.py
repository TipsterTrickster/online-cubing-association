from django.db import models

class Competition(models.Model):
    name = models.CharField(max_length=1000)
    decription = models.CharField(max_length=10000)
    #add more events
    three_by_three = models.BooleanField(default=True)
    date = models.DateField()
    def __str__(self):
        return self.name








