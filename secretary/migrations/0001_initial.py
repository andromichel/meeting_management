# Generated by Django 4.2 on 2024-07-23 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=100)),
                ('member_id', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('meeting_class', models.CharField(choices=[('current_military', 'Current Military'), ('ex_military', 'Ex Military'), ('civilians', 'Civilians')], max_length=20)),
                ('degree', models.CharField(blank=True, max_length=50, null=True)),
                ('purpose', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('rescheduled', 'Rescheduled')], default='pending', max_length=11)),
                ('scheduled_time', models.DateTimeField()),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='secretary.member')),
            ],
        ),
    ]
