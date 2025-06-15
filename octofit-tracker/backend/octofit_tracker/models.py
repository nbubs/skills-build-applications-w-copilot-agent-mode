from django.conf import settings
from bson import ObjectId

# MongoDB models for OctoFit Tracker

class User:
    def __init__(self, email, name, password, _id=None):
        self.email = email
        self.name = name
        self.password = password
        self.id = str(_id) if _id else None

class Team:
    def __init__(self, name, members=None, _id=None):
        self.name = name
        self.members = members or []
        self.id = str(_id) if _id else None

class Activity:
    def __init__(self, user_id, activity_type, duration, timestamp, _id=None):
        self.user_id = user_id
        self.activity_type = activity_type
        self.duration = duration
        self.timestamp = timestamp
        self.id = str(_id) if _id else None

class Leaderboard:
    def __init__(self, team_id, points, _id=None):
        self.team_id = team_id
        self.points = points
        self.id = str(_id) if _id else None

class Workout:
    def __init__(self, user_id, workout_type, details, timestamp, _id=None):
        self.user_id = user_id
        self.workout_type = workout_type
        self.details = details
        self.timestamp = timestamp
        self.id = str(_id) if _id else None
