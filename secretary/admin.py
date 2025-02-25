# admin.py
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile

# Define an inline admin descriptor for Profile model
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

    def save_model(self, request, obj, form, change):
        obj.save()
        if not change:  # If the user is newly created
            Profile.objects.create(user=obj, role='manager')

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
