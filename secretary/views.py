from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import ScheduleMeetingForm, EnterMemberDataForm
from .models import Member, Meeting
from django.urls import reverse
from django.utils import timezone
from django.db.models import Q
from .models import Profile
from .forms import ArabicAuthenticationForm


DEGREE_MAP = {
    'جندي': 'soldier',
    'عريف': 'Corporal',
    'رقيب': 'Sergeant',
    'رقيب أول': 'staff_Sergeant',
    'مساعد': 'assistant',
    'مساعد أول': 'First_Assistant',
    'ملازم': 'lieutenant',
    'ملازم أول': 'first_lieutenant',
    'نقيب': 'captain',
    'رائد': 'major',
    'مقدم': 'lieutenant_colonel',
    'عقيد': 'Colonel',
    'عميد': 'Dean',
    'لواء': 'General',
}

DEPARTMENT_MAP = {
    'سكرتارية السيد المدير': '1st_dep',
    'سكرتارية السيد النائب': '2nd_dep',
    'التعليم': '3rd_dep',
    'الاقسام التعليمية': '4th_dep',
    'كتيبة الطلبة': '5th_dep',
    'الامداد و الاصلاح': '6th_dep',
    'نظم المعلومات': '7th_dep',
    'اركان حرب الكلية': '8th_dep',
    'الامن': '9th_dep',
    'الشئون الادارية': '10th_dep',
    'المسجل': '11th_dep',
    'شئون العاملين': '12th_dep',
    'النقطة الطبية': '13th_dep',
    'القبة السماوية': '14th_dep',
    'الهنجر': '15th_dep',
    'منوب عمليات': '16th_dep',
    'الحملة': '17th_dep',
    'التحويلة': '18th_dep',
    'السلاح': '19th_dep',
    'فوج الجنود': '22th_dep',
}

CLASS_MAP = {
    'عسكريين حاليين': 'current_military',
    'عسكريين سابقين': 'ex_military',
    'مدنيين': 'civilians',
}

def map_search_terms(query):
    query = DEGREE_MAP.get(query, query)
    query = DEPARTMENT_MAP.get(query, query)
    query = CLASS_MAP.get(query, query)
    return query

def login_view(request):
    if request.method == 'POST':
        form = ArabicAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                group = request.POST.get('group')
                request.session['group'] = group  
                return redirect('home')
            else:
                error = 'اسم المستخدم أو كلمة المرور غير صحيحة'
        else:
            error = 'اسم المستخدم أو كلمة المرور غير صحيحة'
    else:
        form = ArabicAuthenticationForm()
        error = None
    return render(request, 'secretary/login.html', {'form': form, 'error': error})

def home_view(request):
    header = 'سكرتارية السيد المدير'
    return render(request, 'secretary/home.html', {'header': header, 'role': 'manager'})


def schedule_meeting_view(request, member_id=None):
    if request.method == 'POST':
        form = ScheduleMeetingForm(request.POST)
        if form.is_valid():
            meeting_data = form.cleaned_data
            member = None
            if member_id:
                member = get_object_or_404(Member, id=member_id)
            
            meeting = Meeting(
                name=member.name if member else meeting_data['name'],
                meeting_class=meeting_data['meeting_class'],
                degree=member.degree if member else meeting_data['degree'],
                department=member.department if member else meeting_data['department'],
                status='pending',
                scheduled_time=timezone.now()
            )
            meeting.save()
            return redirect('pending_meetings')
    else:
        initial_data = {}
        if member_id:
            member = get_object_or_404(Member, id=member_id)
            initial_data = {
                'name': member.name,
                'degree': member.degree,
                'department': member.department
            }
        form = ScheduleMeetingForm(initial=initial_data)
    
    return render(request, 'secretary/schedule_meeting.html', {'form': form, 'member_id': member_id})


def display_members_information_view(request):
    query = request.GET.get('q', '')
    members = Member.objects.all()
    if query:
        query = map_search_terms(query)
        members = members.filter(
            Q(name__icontains=query) |
            Q(degree__icontains=query) |
            Q(department__icontains=query)|
            Q(member_id__icontains=query)
        )
    return render(request, 'secretary/display_members_information.html', {'members': members})


def enter_member_data_view(request):
    if request.method == 'POST':
        form = EnterMemberDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EnterMemberDataForm()
    return render(request, 'secretary/enter_member_data.html', {'form': form})

def pending_meetings_view(request):
    header = 'إجتماعات السيد المدير'
    meetings = Meeting.objects.filter()

    query = request.GET.get('q', '')
    if query:
        query = map_search_terms(query)
        meetings = meetings.filter(
            Q(name__icontains=query) |
            Q(degree__icontains=query) |
            Q(meeting_class__icontains(query)) |
            Q(department__icontains(query))
        )

    return render(request, 'secretary/pending_meetings.html', {'meetings': meetings, 'header': header})



def delete_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    meeting.delete()
    return redirect('pending_meetings')

def edit_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    if request.method == 'POST':
        form = ScheduleMeetingForm(request.POST)
        if form.is_valid():
            meeting_data = form.cleaned_data
            meeting.name = meeting_data['name'] if meeting_data['name'] else meeting.name
            meeting.meeting_class = meeting_data['meeting_class']
            meeting.degree = meeting_data['degree']
            meeting.department = meeting_data['department']
            meeting.save()
            return redirect('pending_meetings')
    else:
        initial_data = {
            'name': meeting.name,
            'meeting_class': meeting.meeting_class,
            'degree': meeting.degree,
            'department': meeting.department,
            'choose_member': meeting.member if hasattr(meeting, 'member') else None,
        }
        form = ScheduleMeetingForm(initial=initial_data)
    return render(request, 'secretary/edit_meeting.html', {'form': form, 'meeting': meeting})

def schedule_meeting_with_member(request, member_id):
    return redirect('schedule_meeting', member_id=member_id)

