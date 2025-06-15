# Serializers for OctoFit Tracker

from rest_framework import serializers

# Placeholder serializers for MongoDB collections

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    email = serializers.EmailField()
    name = serializers.CharField()
    password = serializers.CharField(write_only=True)

class TeamSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    members = serializers.ListField(child=serializers.CharField(), required=False)

class ActivitySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user_id = serializers.CharField()
    activity_type = serializers.CharField()
    duration = serializers.IntegerField()
    timestamp = serializers.DateTimeField()

class LeaderboardSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    team_id = serializers.CharField()
    points = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user_id = serializers.CharField()
    workout_type = serializers.CharField()
    details = serializers.CharField()
    timestamp = serializers.DateTimeField()
