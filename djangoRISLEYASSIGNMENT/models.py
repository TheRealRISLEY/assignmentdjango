from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    email = models.EmailField(max_length=50, blank=True, null=False)
    idnumber = models.IntegerField(max_length=50, blank=True, null=False)
    genre = models.CharField(max_length=50, blank=True, null=False)
    password = models.IntegerField(max_length=50, blank=True, null=False)
    verificationcode = models.IntegerField(max_length=50, blank=True)


def __str__(self):
    return self.name