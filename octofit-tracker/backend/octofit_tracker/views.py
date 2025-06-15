# Views for OctoFit Tracker

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from django.conf import settings

CODESPACE_URL = "https://reimagined-journey-q74xjwxv7p7h4ggq-8000.app.github.dev"
LOCAL_URL = "http://localhost:8000"

class UsersView(APIView):
    def get(self, request):
        users = list(settings.MONGO_DB.users.find())
        for user in users:
            user['id'] = str(user['_id'])
        return Response({
            "codespace_url": f"{CODESPACE_URL}/users/",
            "local_url": f"{LOCAL_URL}/users/",
            "data": UserSerializer(users, many=True).data
        })

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            result = settings.MONGO_DB.users.insert_one(user)
            user['id'] = str(result.inserted_id)
            return Response(user, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamsView(APIView):
    def get(self, request):
        teams = list(settings.MONGO_DB.teams.find())
        for team in teams:
            team['id'] = str(team['_id'])
        return Response({
            "codespace_url": f"{CODESPACE_URL}/teams/",
            "local_url": f"{LOCAL_URL}/teams/",
            "data": TeamSerializer(teams, many=True).data
        })

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            team = serializer.validated_data
            result = settings.MONGO_DB.teams.insert_one(team)
            team['id'] = str(result.inserted_id)
            return Response(team, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivityView(APIView):
    def get(self, request):
        activities = list(settings.MONGO_DB.activity.find())
        for activity in activities:
            activity['id'] = str(activity['_id'])
        return Response({
            "codespace_url": f"{CODESPACE_URL}/activity/",
            "local_url": f"{LOCAL_URL}/activity/",
            "data": ActivitySerializer(activities, many=True).data
        })

    def post(self, request):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            activity = serializer.validated_data
            result = settings.MONGO_DB.activity.insert_one(activity)
            activity['id'] = str(result.inserted_id)
            return Response(activity, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeaderboardView(APIView):
    def get(self, request):
        leaderboard = list(settings.MONGO_DB.leaderboard.find())
        for entry in leaderboard:
            entry['id'] = str(entry['_id'])
        return Response({
            "codespace_url": f"{CODESPACE_URL}/leaderboard/",
            "local_url": f"{LOCAL_URL}/leaderboard/",
            "data": LeaderboardSerializer(leaderboard, many=True).data
        })

    def post(self, request):
        serializer = LeaderboardSerializer(data=request.data)
        if serializer.is_valid():
            entry = serializer.validated_data
            result = settings.MONGO_DB.leaderboard.insert_one(entry)
            entry['id'] = str(result.inserted_id)
            return Response(entry, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkoutsView(APIView):
    def get(self, request):
        workouts = list(settings.MONGO_DB.workouts.find())
        for workout in workouts:
            workout['id'] = str(workout['_id'])
        return Response({
            "codespace_url": f"{CODESPACE_URL}/workouts/",
            "local_url": f"{LOCAL_URL}/workouts/",
            "data": WorkoutSerializer(workouts, many=True).data
        })

    def post(self, request):
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            workout = serializer.validated_data
            result = settings.MONGO_DB.workouts.insert_one(workout)
            workout['id'] = str(result.inserted_id)
            return Response(workout, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
