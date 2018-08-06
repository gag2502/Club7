# -*- coding: utf-8 -*-
from django.db import models

class Workout (models.Model):
    workout = models.CharField(max_length=1)
    sets = models.IntegerField()
    reps= models.IntegerField()
    weight = models.IntegerField()

