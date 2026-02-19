-- ============================================
-- VIEW ALL DATA IN ATTENDANCE MANAGER
-- ============================================
-- Copy and paste this into pgAdmin Query Tool
-- Then press F5 or click Execute button
-- ============================================

-- 1. VIEW ALL USERS
SELECT 'USERS' as table_name, COUNT(*) as total_rows FROM auth_user;
SELECT id, username, email, first_name, is_active, date_joined 
FROM auth_user 
ORDER BY id;

-- 2. VIEW ALL SUBJECTS
SELECT 'SUBJECTS' as table_name, COUNT(*) as total_rows FROM attendance_subject;
SELECT id, name, code, user_id, created_at 
FROM attendance_subject 
ORDER BY name;

-- 3. VIEW ALL LECTURES (TIMETABLE)
SELECT 'LECTURES' as table_name, COUNT(*) as total_rows FROM attendance_lecture;
SELECT l.id, s.name as subject_name, l.day, l.time, l.user_id
FROM attendance_lecture l
JOIN attendance_subject s ON l.subject_id = s.id
ORDER BY l.day, l.time;

-- 4. VIEW ALL ATTENDANCE RECORDS
SELECT 'ATTENDANCE RECORDS' as table_name, COUNT(*) as total_rows FROM attendance_attendancerecord;
SELECT r.id, s.name as subject_name, r.date, r.status, r.lecture_time
FROM attendance_attendancerecord r
JOIN attendance_subject s ON r.subject_id = s.id
ORDER BY r.date DESC;

-- 5. VIEW USER SETTINGS
SELECT 'USER SETTINGS' as table_name, COUNT(*) as total_rows FROM attendance_usersetting;
SELECT us.id, u.username, us.target_percentage
FROM attendance_usersetting us
JOIN auth_user u ON us.user_id = u.id;

-- 6. SUMMARY OF ALL DATA
SELECT 
    'Users' as category, COUNT(*) as count FROM auth_user
UNION ALL
SELECT 
    'Subjects', COUNT(*) FROM attendance_subject
UNION ALL
SELECT 
    'Lectures', COUNT(*) FROM attendance_lecture
UNION ALL
SELECT 
    'Attendance Records', COUNT(*) FROM attendance_attendancerecord
UNION ALL
SELECT 
    'User Settings', COUNT(*) FROM attendance_usersetting;

-- ============================================
-- END OF QUERIES
-- ============================================
