from django.core.management.base import BaseCommand

from octofit_tracker.models import Activity, FitnessUser, Leaderboard, Team, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        for model in [FitnessUser, Team, Activity, Leaderboard, Workout]:
            try:
                model.objects.all().delete()
            except Exception:
                pass

        Team.objects.create(name='Marvel', city='New York')
        Team.objects.create(name='DC', city='Gotham')

        FitnessUser.objects.create(
            username='ironman',
            email='ironman@marvel.com',
            hero_name='Iron Man',
            team='Marvel',
        )
        FitnessUser.objects.create(
            username='spiderman',
            email='spiderman@marvel.com',
            hero_name='Spider-Man',
            team='Marvel',
        )
        FitnessUser.objects.create(
            username='batman',
            email='batman@dc.com',
            hero_name='Batman',
            team='DC',
        )
        FitnessUser.objects.create(
            username='superman',
            email='superman@dc.com',
            hero_name='Superman',
            team='DC',
        )

        Activity.objects.create(
            hero_name='Iron Man',
            activity_type='Repulsor Run',
            duration_minutes=45,
            calories_burned=540,
        )
        Activity.objects.create(
            hero_name='Batman',
            activity_type='Rooftop Sprint',
            duration_minutes=35,
            calories_burned=410,
        )

        Workout.objects.create(
            hero_name='Spider-Man',
            title='Wall-Crawl Circuit',
            details='Pull-ups, agility ladder, and mobility work',
        )
        Workout.objects.create(
            hero_name='Superman',
            title='Fortress Strength Set',
            details='Deadlifts, farmer carries, and interval sprints',
        )

        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=80)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
