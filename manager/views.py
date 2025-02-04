from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from secretary.models import Meeting


@login_required
def meeting_list_view(request):
    meetings = Meeting.objects.filter(status='pending')  # Only get pending meetings
    return render(request, 'manager/meeting_list.html', {'meetings': meetings})

@login_required
def approve_meeting_view(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    meeting.status = 'approved'
    meeting.save()
    return redirect('meeting_list')

@login_required
def reject_meeting_view(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    meeting.status = 'rejected'
    meeting.save()
    return redirect('meeting_list')
