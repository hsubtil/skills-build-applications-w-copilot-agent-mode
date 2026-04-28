import os

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from octofit_tracker.views import (
    ActivityViewSet,
    FitnessUserViewSet,
    LeaderboardViewSet,
    TeamViewSet,
    WorkoutViewSet,
    api_root,
)

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = 'http://localhost:8000'

router = DefaultRouter()
router.register('users', FitnessUserViewSet, basename='users')
router.register('teams', TeamViewSet, basename='teams')
router.register('activities', ActivityViewSet, basename='activities')
router.register('leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register('workouts', WorkoutViewSet, basename='workouts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
