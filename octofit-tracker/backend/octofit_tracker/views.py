from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from octofit_tracker.models import Activity, FitnessUser, Leaderboard, Team, Workout
from octofit_tracker.serializers import (
    ActivitySerializer,
    FitnessUserSerializer,
    LeaderboardSerializer,
    TeamSerializer,
    WorkoutSerializer,
)


class FitnessUserViewSet(viewsets.ModelViewSet):
    queryset = FitnessUser.objects.all().order_by('username')
    serializer_class = FitnessUserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('hero_name')
    serializer_class = ActivitySerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all().order_by('-points')
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all().order_by('hero_name')
    serializer_class = WorkoutSerializer


@api_view(['GET'])
def api_root(request):
    return Response(
        {
            'users': request.build_absolute_uri('/api/users/'),
            'teams': request.build_absolute_uri('/api/teams/'),
            'activities': request.build_absolute_uri('/api/activities/'),
            'leaderboard': request.build_absolute_uri('/api/leaderboard/'),
            'workouts': request.build_absolute_uri('/api/workouts/'),
        }
    )