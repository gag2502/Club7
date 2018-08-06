# -*- coding: utf-8 -*-
from django.shortcuts import render
from club7.workout.models import Workout
from club7.workout.serializers import WorkoutSerializer
from rest_framework.response import response
from rest_framework.viewsets import viewsets

class WorkoutViewSet (viewsets.ModelViewSet):
    
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


