from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    idnumber = models.IntegerField(blank=True, null=False)
    ticketprice = models.IntegerField(blank=True, null=False)
    ticketnumber = models.CharField(max_length=50, blank=True, null=False)
    date = models.IntegerField(blank=True, null=False)



def __str__(self):
    return self.name