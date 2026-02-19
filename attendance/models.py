from django.contrib.auth.models import User
from django.db import models


class Subject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'name')
        ordering = ('name',)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    DAYS = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lectures')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='lectures')
    day = models.CharField(max_length=10, choices=DAYS)
    time = models.TimeField()

    class Meta:
        unique_together = ('user', 'subject', 'day', 'time')
        ordering = ('day', 'time')


class AttendanceRecord(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('off', 'Off'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='records')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='records')
    date = models.DateField()
    lecture_time = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('user', 'subject', 'date', 'lecture_time')
        ordering = ('-date',)


class UserSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='attendance_setting')
    target_percentage = models.PositiveSmallIntegerField(default=80)

    def __str__(self):
        return f'{self.user.username}: {self.target_percentage}%'
