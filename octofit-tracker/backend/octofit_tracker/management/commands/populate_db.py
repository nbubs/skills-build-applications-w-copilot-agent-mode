from django.core.management.base import BaseCommand
from django.conf import settings
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate octofit_db with test data.'

    def handle(self, *args, **kwargs):
        db = settings.MONGO_DB
        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Test users
        users = [
            {"email": "alice@example.com", "name": "Alice", "password": "alicepass"},
            {"email": "bob@example.com", "name": "Bob", "password": "bobpass"},
            {"email": "carol@example.com", "name": "Carol", "password": "carolpass"}
        ]
        db.users.insert_many(users)

        # Test teams
        teams = [
            {"name": "Team Alpha", "members": ["alice@example.com", "bob@example.com"]},
            {"name": "Team Beta", "members": ["carol@example.com"]}
        ]
        db.teams.insert_many(teams)

        # Test activities
        activities = [
            {"user_id": "alice@example.com", "activity_type": "run", "duration": 30, "timestamp": datetime(2025, 6, 1)},
            {"user_id": "bob@example.com", "activity_type": "walk", "duration": 60, "timestamp": datetime(2025, 6, 2)},
            {"user_id": "carol@example.com", "activity_type": "cycle", "duration": 45, "timestamp": datetime(2025, 6, 3)}
        ]
        db.activity.insert_many(activities)

        # Test leaderboard
        leaderboard = [
            {"team_id": "Team Alpha", "points": 100},
            {"team_id": "Team Beta", "points": 80}
        ]
        db.leaderboard.insert_many(leaderboard)

        # Test workouts
        workouts = [
            {"user_id": "alice@example.com", "workout_type": "cardio", "details": "30 min run", "timestamp": datetime(2025, 6, 1)},
            {"user_id": "bob@example.com", "workout_type": "strength", "details": "pushups", "timestamp": datetime(2025, 6, 2)},
            {"user_id": "carol@example.com", "workout_type": "yoga", "details": "morning yoga", "timestamp": datetime(2025, 6, 3)}
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Test data populated in octofit_db.'))
