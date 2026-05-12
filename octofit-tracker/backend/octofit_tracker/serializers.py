"""Serializers convert model instances (including MongoDB ObjectId fields) to JSON."""
from rest_framework import serializers
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'age']

    def get_id(self, obj):
        return str(obj.pk)


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'members']

    def get_id(self, obj):
        return str(obj.pk)


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'timestamp']

    def get_id(self, obj):
        return str(obj.pk)


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'score']

    def get_id(self, obj):
        return str(obj.pk)


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Workout
        fields = ['id', 'name', 'description']

    def get_id(self, obj):
        return str(obj.pk)
