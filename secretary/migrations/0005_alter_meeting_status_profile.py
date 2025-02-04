# Generated by Django 4.2.14 on 2024-08-06 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('secretary', '0004_remove_meeting_purpose_alter_meeting_scheduled_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='status',
            field=models.CharField(choices=[('pending', 'قيد الإنتظار'), ('approved', 'مقبول'), ('rejected', 'مرفوض'), ('rescheduled', 'Rescheduled')], default='pending', max_length=11),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('manager', 'Manager'), ('vice_manager', 'Vice Manager')], max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
