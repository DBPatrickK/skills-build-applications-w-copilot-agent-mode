from django.core.management.base import BaseCommand
from octofit_tracker.api import models

class Command(BaseCommand):
    help = 'Populate the octofit_db MongoDB database with test data.'

    def handle(self, *args, **options):
        # Create test Team
        team, created = models.Team.objects.get_or_create(name='Test Team')
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created team: {team.name}'))
        else:
            self.stdout.write('Test team already exists.')

        # Create test User
        user, created = models.User.objects.get_or_create(email='testuser@example.com', defaults={'name': 'Test User', 'team': team.name})
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created user: {user.name}'))
        else:
            self.stdout.write('Test user already exists.')

        # Create test Activity
        activity, created = models.Activity.objects.get_or_create(user=user.name, type='Running', duration=30, date='2024-01-01')
        if created:
            self.stdout.write(self.style.SUCCESS('Created activity.'))
        else:
            self.stdout.write('Test activity already exists.')

        # Create test Leaderboard
        leaderboard, created = models.Leaderboard.objects.get_or_create(team=team.name, points=100)
        if created:
            self.stdout.write(self.style.SUCCESS('Created leaderboard entry.'))
        else:
            self.stdout.write('Leaderboard entry already exists.')

        # Create test Workout
        workout, created = models.Workout.objects.get_or_create(name='Push Ups', defaults={'description': 'Do 20 push ups', 'difficulty': 'Easy'})
        if created:
            self.stdout.write(self.style.SUCCESS('Created workout.'))
        else:
            self.stdout.write('Workout already exists.')

        self.stdout.write(self.style.SUCCESS('Test data population complete.'))
