"""Tests for the OctoFit Tracker app."""
from django.test import TestCase
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


class OctofitModelsTest(TestCase):
    def test_user_str(self):
        user = User(email='alice@example.com', name='Alice')
        self.assertEqual(str(user), 'Alice')

    def test_team_str(self):
        team = Team(name='Mergington High School')
        self.assertEqual(str(team), 'Mergington High School')
