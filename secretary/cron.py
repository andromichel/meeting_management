# meeting_management/cron.py
from .models import Meeting

def clear_pending_meetings():
    Meeting.objects.filter(status='pending').delete()
