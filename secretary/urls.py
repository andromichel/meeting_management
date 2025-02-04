from django.urls import path
from .views import login_view, home_view, schedule_meeting_view, enter_member_data_view, display_members_information_view, pending_meetings_view,  delete_meeting, edit_meeting, schedule_meeting_with_member


urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('schedule_meeting/', schedule_meeting_view, name='schedule_meeting'),
    path('schedule_meeting/<int:member_id>/', schedule_meeting_view, name='schedule_meeting'),
    path('enter_member_data/', enter_member_data_view, name='enter_member_data'),
    path('display_members_information/', display_members_information_view, name='display_members_information'),
    path('pending-meetings/', pending_meetings_view, name='pending_meetings'),
    path('delete_meeting/<int:meeting_id>/', delete_meeting, name='delete_meeting'),
    path('edit_meeting/<int:meeting_id>/', edit_meeting, name='edit_meeting'),
    path('schedule_meeting_with_member/<int:member_id>/', schedule_meeting_with_member, name='schedule_meeting_with_member'),


]

    


