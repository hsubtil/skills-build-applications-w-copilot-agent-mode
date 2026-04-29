from djongo import models


class FitnessUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    hero_name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.hero_name


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class Activity(models.Model):
    hero_name = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    calories_burned = models.IntegerField()

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.hero_name} - {self.activity_type}"


class Leaderboard(models.Model):
    team = models.CharField(max_length=100, unique=True)
    points = models.IntegerField()

    class Meta:
        db_table = 'leaderboard'

    def __str__(self):
        return f"{self.team}: {self.points}"


class Workout(models.Model):
    hero_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    details = models.TextField()

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.title
