from django.urls import path

from . import views

urlpatterns = [
    path('auth/register/', views.register_view, name='register'),
    path('auth/login/', views.login_view, name='login'),
    path('auth/logout/', views.logout_view, name='logout'),
    path('auth/me/', views.me_view, name='me'),
    path('subjects/', views.subjects_view, name='subjects'),
    path('subjects/<int:subject_id>/', views.subject_detail_view, name='subject-detail'),
    path('lectures/', views.lectures_view, name='lectures'),
    path('lectures/<int:lecture_id>/', views.lecture_detail_view, name='lecture-detail'),
    path('records/', views.records_view, name='records'),
    path('records/<int:record_id>/', views.record_detail_view, name='record-detail'),
    path('settings/', views.settings_view, name='settings'),
    path('dashboard/summary/', views.dashboard_summary_view, name='dashboard-summary'),
]
