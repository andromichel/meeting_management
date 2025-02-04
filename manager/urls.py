from django.urls import path
from . import views

urlpatterns = [
    path('', views.meeting_list_view, name='meeting_list'),
    path('approve/<int:meeting_id>/', views.approve_meeting_view, name='approve_meeting'),
    path('reject/<int:meeting_id>/', views.reject_meeting_view, name='reject_meeting'),
]
