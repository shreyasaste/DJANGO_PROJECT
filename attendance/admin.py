from django.contrib import admin

from .models import AttendanceRecord, Lecture, Subject, UserSetting

admin.site.register(Subject)
admin.site.register(Lecture)
admin.site.register(AttendanceRecord)
admin.site.register(UserSetting)
