# Tests for OctoFit Tracker

from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User(email="test@example.com", name="Test User", password="pass123")
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team(name="Team A", members=["user1", "user2"])
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity(user_id="user1", activity_type="run", duration=30, timestamp="2025-06-15T00:00:00Z")
        self.assertEqual(activity.activity_type, "run")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard(team_id="team1", points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout(user_id="user1", workout_type="cardio", details="30 min run", timestamp="2025-06-15T00:00:00Z")
        self.assertEqual(workout.workout_type, "cardio")
