from django.db import models

class Comp(models.Model):
    name = models.CharField(max_length=250)
    compid = models.CharField(max_length=12)
    compcountry = models.CharField(max_length=100, default='DEFAULT VALUE')
    compstate = models.CharField(max_length=100, default='DEFAULT VALUE')
    compgender = models.CharField(max_length=10, default='DEFAULT VALUE')
    compcomp = models.CharField(max_length=100000, default='DEFAULT VALUE')
    compsolves = models.CharField(max_length=1000000, default='DEFAULT VALUE')
    GN = models.CharField(max_length=50, default='0')
    SN = models.CharField(max_length=50, default='0')
    BN = models.CharField(max_length=50, default='0')
    ORN = models.CharField(max_length=50, default='0')
    RRN = models.CharField(max_length=50, default='0')
    SRN = models.CharField(max_length=50, default='0')

    def __str__(self):
        return self.name

class Compdetails(models.Model):
    competitor_name = models.ForeignKey(Comp, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=50)
    pb_single = models.CharField(max_length=50, default='')
    pb_average = models.CharField(max_length=50, default='')
    ORA = models.CharField(max_length=50, default='n/a')
    ORS = models.CharField(max_length=50, default='n/a')
    def __str__(self):
        return self.event_name


