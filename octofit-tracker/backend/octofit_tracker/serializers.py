from rest_framework import serializers

from octofit_tracker.models import Activity, FitnessUser, Leaderboard, Team, Workout


class ObjectIdStringMixin(serializers.ModelSerializer):
    mongo_id = serializers.SerializerMethodField()

    def get_mongo_id(self, obj):
        mongo_id = getattr(obj, '_id', None)
        return str(mongo_id) if mongo_id is not None else None


class FitnessUserSerializer(ObjectIdStringMixin):
    class Meta:
        model = FitnessUser
        fields = ['id', 'mongo_id', 'username', 'email', 'hero_name', 'team']


class TeamSerializer(ObjectIdStringMixin):
    class Meta:
        model = Team
        fields = ['id', 'mongo_id', 'name', 'city']


class ActivitySerializer(ObjectIdStringMixin):
    class Meta:
        model = Activity
        fields = ['id', 'mongo_id', 'hero_name', 'activity_type', 'duration_minutes', 'calories_burned']


class LeaderboardSerializer(ObjectIdStringMixin):
    class Meta:
        model = Leaderboard
        fields = ['id', 'mongo_id', 'team', 'points']


class WorkoutSerializer(ObjectIdStringMixin):
    class Meta:
        model = Workout
        fields = ['id', 'mongo_id', 'hero_name', 'title', 'details']