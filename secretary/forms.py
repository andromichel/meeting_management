from django import forms
from .models import Meeting, Member
from django.contrib.auth.forms import AuthenticationForm


class ArabicAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='اسم المستخدم')
    password = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput)

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['name', 'meeting_class', 'degree']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'degree', 'department', 'member_id']

class ScheduleMeetingForm(forms.Form):
    name = forms.CharField(label='الاسم', max_length=100, required=True)
    meeting_class = forms.ChoiceField(choices=Meeting.CLASS_CHOICES, label='الدرجة')   
    degree = forms.ChoiceField(choices=Member.DEGREE_CHOICES, required=False, label='الرتبة')
    department = forms.ChoiceField(choices=Member.DEPARTMENT_CHOICES, required=False, label='القسم')

class MemberSelectionForm(forms.Form):
    member = forms.ModelChoiceField(queryset=Member.objects.all(), required=False, label='اختر العضو')    

class EnterMemberDataForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'degree', 'department', 'member_id']
        labels = {
            'name': 'الاسم',
            'degree': 'الرتبة',
            'department': 'القسم',
            'member_id': 'الرقم العسكري',
        }
