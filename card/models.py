from django.db import models

class Rate(models.Model):
    gold = models.CharField(max_length=10)
    silver = models.CharField(max_length=10)