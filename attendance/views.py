import json
from datetime import datetime
from functools import wraps

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import AttendanceRecord, Lecture, Subject, UserSetting


def parse_json(request):
    try:
        return json.loads(request.body.decode('utf-8')) if request.body else {}
    except json.JSONDecodeError:
        return None


def login_required_api(view_func):
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return view_func(request, *args, **kwargs)

    return _wrapped


def subject_to_dict(subject):
    return {'id': subject.id, 'name': subject.name, 'code': subject.code}


def lecture_to_dict(lecture):
    return {
        'id': lecture.id,
        'subject_id': lecture.subject_id,
        'day': lecture.day,
        'time': lecture.time.strftime('%H:%M'),
    }


def record_to_dict(record):
    return {
        'id': record.id,
        'subject_id': record.subject_id,
        'date': record.date.isoformat(),
        'lecture_time': record.lecture_time.strftime('%H:%M') if record.lecture_time else None,
        'status': record.status,
    }


@csrf_exempt
@require_http_methods(['POST'])
def register_view(request):
    payload = parse_json(request)
    if payload is None:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    name = (payload.get('name') or '').strip()
    email = (payload.get('email') or '').strip().lower()
    password = payload.get('password') or ''

    if not name or not email or not password:
        return JsonResponse({'error': 'name, email and password are required'}, status=400)

    if User.objects.filter(username=email).exists():
        return JsonResponse({'error': 'Email already registered'}, status=409)

    user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
    UserSetting.objects.get_or_create(user=user)
    login(request, user)
    return JsonResponse({'message': 'Account created', 'user': {'name': user.first_name, 'email': user.email}}, status=201)


@csrf_exempt
@require_http_methods(['POST'])
def login_view(request):
    payload = parse_json(request)
    if payload is None:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    email = (payload.get('email') or '').strip().lower()
    password = payload.get('password') or ''

    user = authenticate(request, username=email, password=password)
    if not user:
        return JsonResponse({'error': 'Invalid credentials'}, status=401)

    login(request, user)
    return JsonResponse({'message': 'Logged in', 'user': {'name': user.first_name, 'email': user.email}})


@csrf_exempt
@require_http_methods(['POST'])
@login_required_api
def logout_view(request):
    logout(request)
    # Clear the session completely
    request.session.flush()
    return JsonResponse({'message': 'Logged out'})


@require_http_methods(['GET'])
@login_required_api
def me_view(request):
    setting, _ = UserSetting.objects.get_or_create(user=request.user)
    return JsonResponse(
        {
            'user': {'name': request.user.first_name, 'email': request.user.email},
            'target_percentage': setting.target_percentage,
        }
    )


@csrf_exempt
@require_http_methods(['GET', 'POST'])
@login_required_api
def subjects_view(request):
    if request.method == 'GET':
        subjects = Subject.objects.filter(user=request.user)
        return JsonResponse({'subjects': [subject_to_dict(s) for s in subjects]})

    payload = parse_json(request)
    if payload is None:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    name = (payload.get('name') or '').strip()
    code = (payload.get('code') or '').strip()
    if not name:
        return JsonResponse({'error': 'name is required'}, status=400)

    subject, created = Subject.objects.get_or_create(user=request.user, name=name, defaults={'code': code})
    if not created and code and subject.code != code:
        subject.code = code
        subject.save(update_fields=['code'])

    return JsonResponse({'subject': subject_to_dict(subject), 'created': created}, status=201 if created else 200)


@csrf_exempt
@require_http_methods(['PUT', 'DELETE'])
@login_required_api
def subject_detail_view(request, subject_id):
    try:
        subject = Subject.objects.get(id=subject_id, user=request.user)
    except Subject.DoesNotExist:
        return JsonResponse({'error': 'Subject not found'}, status=404)

    if request.method == 'DELETE':
        subject.delete()
        return JsonResponse({'message': 'Subject deleted'})

    payload = parse_json(request)
    if payload is None:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    name = (payload.get('name') or '').strip()
    code = (payload.get('code') or '').strip()

    if name:
        subject.name = name
    subject.code = code
    subject.save()
    return JsonResponse({'subject': subject_to_dict(subject)})


@csrf_exempt
@require_http_methods(['GET', 'POST'])
@login_required_api
def lectures_view(request):
    if request.method == 'GET':
        day = (request.GET.get('day') or '').strip().lower()
        lectures = Lecture.objects.filter(user=request.user)
        if day:
            lectures = lectures.filter(day=day)
        return JsonResponse({'lectures': [lecture_to_dict(l) for l in lectures]})

    payload = parse_json(request)
    if payload is None:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    subject_id = payload.get('subject_id')
    day = (payload.get('day') or '').strip().lower()
    time_value = (payload.get('time') or '').strip()

    if not subject_id or not day or not time_value:
        return JsonResponse({'error': 'subject_id, day, time are required'}, status=400)

    try:
        subject = Subject.objects.get(id=subject_id, user=request.user)
    except Subject.DoesNotExist:
        return JsonResponse({'error': 'Subject not found'}, status=404)

    try:
        time_obj = datetime.strptime(time_value, '%H:%M').time()
    except ValueError:
        return JsonResponse({'error': 'time must be HH:MM'}, status=400)

    lecture, created = Lecture.objects.get_or_create(
        user=request.user,
        subject=subject,
        day=day,
        time=time_obj,
    )

    return JsonResponse({'lecture': lecture_to_dict(lecture), 'created': created}, status=201 if created else 200)


@csrf_exempt
@require_http_methods(['DELETE'])
@login_required_api
def lecture_detail_view(request, lecture_id):
    deleted, _ = Lecture.objects.filter(id=lecture_id, user=request.user).delete()
    if not deleted:
        return JsonResponse({'error': 'Lecture not found'}, status=404)
    return JsonResponse({'message': 'Lecture deleted'})


@csrf_exempt
@require_http_methods(['GET', 'POST'])
@login_required_api
def records_view(request):
    if request.method == 'GET':
        date_str = (request.GET.get('date') or '').strip()
        records = AttendanceRecord.objects.filter(user=request.user)
        if date_str:
            records = records.filter(date=date_str)
        return JsonResponse({'records': [record_to_dict(r) for r in records]})

    payload = parse_json(request)
    if payload is None:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    subject_id = payload.get('subject_id')
    date_value = (payload.get('date') or '').strip()
    status = (payload.get('status') or '').strip().lower()
    lecture_time_value = payload.get('lecture_time')

    if not subject_id or not date_value or status not in {'present', 'absent', 'off'}:
        return JsonResponse({'error': 'subject_id, date and valid status are required'}, status=400)

    try:
        subject = Subject.objects.get(id=subject_id, user=request.user)
    except Subject.DoesNotExist:
        return JsonResponse({'error': 'Subject not found'}, status=404)

    lecture_time = None
    if lecture_time_value:
        try:
            lecture_time = datetime.strptime(lecture_time_value, '%H:%M').time()
        except ValueError:
            return JsonResponse({'error': 'lecture_time must be HH:MM'}, status=400)

    try:
        date_obj = datetime.strptime(date_value, '%Y-%m-%d').date()
    except ValueError:
        return JsonResponse({'error': 'date must be YYYY-MM-DD'}, status=400)

    record, created = AttendanceRecord.objects.update_or_create(
        user=request.user,
        subject=subject,
        date=date_obj,
        lecture_time=lecture_time,
        defaults={'status': status},
    )
    return JsonResponse({'record': record_to_dict(record), 'created': created}, status=201 if created else 200)


@csrf_exempt
@require_http_methods(['DELETE'])
@login_required_api
def record_detail_view(request, record_id):
    deleted, _ = AttendanceRecord.objects.filter(id=record_id, user=request.user).delete()
    if not deleted:
        return JsonResponse({'error': 'Record not found'}, status=404)
    return JsonResponse({'message': 'Record deleted'})


@csrf_exempt
@require_http_methods(['GET', 'PUT'])
@login_required_api
def settings_view(request):
    setting, _ = UserSetting.objects.get_or_create(user=request.user)

    if request.method == 'GET':
        return JsonResponse({'target_percentage': setting.target_percentage})

    payload = parse_json(request)
    if payload is None:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    target = payload.get('target_percentage')
    if not isinstance(target, int) or target < 1 or target > 100:
        return JsonResponse({'error': 'target_percentage must be 1..100'}, status=400)

    setting.target_percentage = target
    setting.save(update_fields=['target_percentage'])
    return JsonResponse({'target_percentage': setting.target_percentage})


@require_http_methods(['GET'])
@login_required_api
def dashboard_summary_view(request):
    records = AttendanceRecord.objects.filter(user=request.user)
    total = records.filter(Q(status='present') | Q(status='absent')).count()
    attended = records.filter(status='present').count()
    missed = records.filter(status='absent').count()
    percentage = int(round((attended / total) * 100)) if total else 0

    by_subject = (
        records.values('subject__id', 'subject__name')
        .annotate(
            present=Count('id', filter=Q(status='present')),
            absent=Count('id', filter=Q(status='absent')),
        )
        .order_by('subject__name')
    )

    subjects = []
    for row in by_subject:
        subject_total = row['present'] + row['absent']
        subject_percentage = int(round((row['present'] / subject_total) * 100)) if subject_total else 0
        subjects.append(
            {
                'subject_id': row['subject__id'],
                'subject_name': row['subject__name'],
                'present': row['present'],
                'absent': row['absent'],
                'percentage': subject_percentage,
            }
        )

    return JsonResponse(
        {
            'overall': {
                'total': total,
                'attended': attended,
                'missed': missed,
                'percentage': percentage,
            },
            'subjects': subjects,
        }
    )
