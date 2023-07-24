from django.db import models

# Create your models here.

class Question(models.Model):
    qtext = models.CharField(max_length=250)
    c1 = models.CharField(max_length=250)
    c2 = models.CharField(max_length=250)
    c3 = models.CharField(max_length=250)
    c4 = models.CharField(max_length=250)
    ans = models.CharField(max_length=250)
