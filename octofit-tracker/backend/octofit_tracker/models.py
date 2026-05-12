"""Models for the OctoFit Tracker app stored in octofit_db (MongoDB via djongo)."""
from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='teams', blank=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField(help_text='Duration in minutes')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.activity_type}"


class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.name}: {self.score}"


class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
