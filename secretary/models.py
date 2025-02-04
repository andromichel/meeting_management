from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, default='manager')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Member(models.Model):
    DEGREE_CHOICES = [
        ('soldier', 'جندي'),
        ('Corporal', 'عريف'),
        ('Sergeant', 'رقيب'),
        ('staff_Sergeant', 'رقيب أول'),
        ('assistant', 'مساعد'),
        ('First_Assistant', 'مساعد أول'),
        ('lieutenant', 'ملازم'),
        ('first_lieutenant', 'ملازم أول'),
        ('captain', 'نقيب'),
        ('major', 'رائد'),
        ('lieutenant_colonel', 'مقدم'),
        ('Colonel', 'عقيد'),
        ('Dean', 'عميد'),
        ('General', 'لواء'),
    ]

    DEPARTMENT_CHOICES = [
        ('1st_dep', 'سكرتارية السيد المدير'),
        ('2nd_dep', 'سكرتارية السيد النائب'),
        ('3rd_dep', 'التعليم'),
        ('4th_dep', 'الاقسام التعليمية'),
        ('5th_dep', 'كتيبة الطلبة'),
        ('6th_dep', 'الامداد و الاصلاح'),
        ('7th_dep', 'نظم المعلومات'),
        ('8th_dep', 'اركان حرب  الكلية'),
        ('9th_dep', 'الامن'),
        ('10th_dep', 'الشئون الادارية'),
        ('11th_dep', 'المسجل'),
        ('12th_dep', 'شئون العاملين'),
        ('13th_dep', 'النقطة الطبية'),
        ('14th_dep', 'القبة السماوية'),
        ('15th_dep', 'الهنجر'),
        ('16th_dep', 'منوب عمليات'),
        ('17th_dep', 'الحملة'),
        ('18th_dep', 'التحويلة'),
        ('19th_dep', 'السلاح'),
        ('22th_dep', 'فوج الجنود'),
    ]

    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    member_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class Meeting(models.Model):
    STATUS_CHOICES = [
        ('pending', 'قيد الإنتظار'),
        ('approved', 'مقبول'),
        ('rejected', 'مرفوض'),
        ('rescheduled', 'Rescheduled'),
    ]

    CLASS_CHOICES = [
        ('current_military', 'عسكريين حاليين'),
        ('ex_military', 'عسكريين سابقين'),
        ('civilians', 'مدنيين'),
    ]

    name = models.CharField(max_length=100)
    meeting_class = models.CharField(max_length=20, choices=CLASS_CHOICES)
    degree = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=100, choices=Member.DEPARTMENT_CHOICES, blank=True, null=True)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default='pending')
    scheduled_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

