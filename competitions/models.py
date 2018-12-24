from django.db import models

class Competition(models.Model):
    name = models.CharField(max_length=1000)
    decription = models.CharField(max_length=10000)
    #add more events
    three_by_three = models.BooleanField(default=True)
    two_by_two = models.BooleanField(default=False)
    four_by_four = models.BooleanField(default=False)
    five_by_five = models.BooleanField(default=False)
    six_by_six = models.BooleanField(default=False)
    seven_by_seven = models.BooleanField(default=False)
    three_blind = models.BooleanField(default=False)
    FMC = models.BooleanField(default=False)
    One_Handed = models.BooleanField(default=False)
    Feet = models.BooleanField(default=False)
    Clock = models.BooleanField(default=False)
    Megaminx = models.BooleanField(default=False)
    Pyraminx = models.BooleanField(default=False)
    Skewb = models.BooleanField(default=False)
    Square_1 = models.BooleanField(default=False)
    four_blind = models.BooleanField(default=False)
    five_blind = models.BooleanField(default=False)
    multi_blind = models.BooleanField(default=False)
    date = models.DateField()
    def __str__(self):
        return self.name








