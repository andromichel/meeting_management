from django.core.management.base import BaseCommand
from secretary.models import Meeting
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Clear meetings data every 24 hours'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        one_day_ago = now - timedelta(days=1)
        # Clear all meetings older than one day
        Meeting.objects.filter(scheduled_time__lt=one_day_ago).delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared meetings older than 24 hours'))