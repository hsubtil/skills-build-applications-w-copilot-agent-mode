from django.test import TestCase
from .models import FitnessUser, Team, Activity, Leaderboard, Workout

class FitnessUserModelTest(TestCase):
    def test_create_user(self):
        user = FitnessUser.objects.create(username='testuser', email='test@example.com', hero_name='Test Hero', team='Test Team')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team', city='Test City')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(hero_name='Test Hero', activity_type='Run', duration_minutes=30, calories_burned=300)
        self.assertEqual(activity.activity_type, 'Run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='Test Team', points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(hero_name='Test Hero', title='Morning Routine', details='Pushups, Situps')
        self.assertEqual(workout.title, 'Morning Routine')
