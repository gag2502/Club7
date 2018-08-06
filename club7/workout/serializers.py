from rest_framework import serializers

class WorkoutSerialize (serializers.Serializer):
    workout = serializers.CharField(max_length=1)
    sets = serializers.IntegerField()
    reps= serializers.IntegerField()
    weight = serializers.IntegerField()