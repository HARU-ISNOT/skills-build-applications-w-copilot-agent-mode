"""
Django management command to Populate the octofit_db database with test data.

This command seeds the octofit_db MongoDB database (via djongo) with sample users,
teams, activities, leaderboard entries, and workout suggestions so the OctoFit
Tracker app has data to display from the very first run.
"""
from django.core.management.base import BaseCommand

from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data for the OctoFit Tracker app.'

    def handle(self, *args, **options):
        # Populate the octofit_db database with test data: clear existing rows first
        # so the command is idempotent when re-run during development.
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Users
        alice = User.objects.create(email='alice@mergington.edu', name='Alice', age=16)
        bob = User.objects.create(email='bob@mergington.edu', name='Bob', age=17)
        carol = User.objects.create(email='carol@mergington.edu', name='Carol', age=16)

        # Team
        team = Team.objects.create(name='Mergington High School Eagles')
        team.members.add(alice, bob, carol)

        # Activities
        Activity.objects.create(user=alice, activity_type='Running', duration=30)
        Activity.objects.create(user=bob, activity_type='Cycling', duration=45)
        Activity.objects.create(user=carol, activity_type='Swimming', duration=40)

        # Leaderboard
        Leaderboard.objects.create(user=alice, score=120)
        Leaderboard.objects.create(user=bob, score=95)
        Leaderboard.objects.create(user=carol, score=110)

        # Workout suggestions
        Workout.objects.create(
            name='Morning Sprint',
            description='10x100m sprints with 30s rest to build explosive speed.',
        )
        Workout.objects.create(
            name='Cycling Endurance',
            description='45 min steady-state cycling at moderate intensity.',
        )

        self.stdout.write(
            self.style.SUCCESS('Successfully populated the octofit_db database with test data.')
        )
