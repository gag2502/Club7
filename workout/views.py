# -*- coding: utf-8 -*-
from django.shortcuts import render
from workout.models import Workout
from workout.serializers import WorkoutSerializer
from rest_framework import response
from rest_framework import viewsets

class WorkoutViewSet (viewsets.ModelViewSet):
    
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


