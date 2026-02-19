// Attendance Manager - API Integration
// This replaces localStorage with Django REST API calls

const API_BASE = 'http://127.0.0.1:8000/api';

// API Helper Functions
async function apiCall(endpoint, method = 'GET', body = null) {
    const options = {
        method,
        credentials: 'include',
        headers: { 'Content-Type': 'application/json' }
    };
    if (body) options.body = JSON.stringify(body);
    
    try {
        const res = await fetch(`${API_BASE}${endpoint}`, options);
        const data = await res.json();
        if (!res.ok) throw new Error(data.error || 'API Error');
        return data;
    } catch (err) {
        console.error('API Error:', err);
        throw err;
    }
}

// Authentication API
const AuthAPI = {
    async register(name, email, password) {
        return await apiCall('/auth/register/', 'POST', { name, email, password });
    },
    
    async login(email, password) {
        return await apiCall('/auth/login/', 'POST', { email, password });
    },
    
    async logout() {
        return await apiCall('/auth/logout/', 'POST');
    },
    
    async getMe() {
        return await apiCall('/auth/me/');
    }
};

// Subjects API
const SubjectsAPI = {
    async getAll() {
        const data = await apiCall('/subjects/');
        return data.subjects;
    },
    
    async create(name, code = '') {
        const data = await apiCall('/subjects/', 'POST', { name, code });
        return data.subject;
    },
    
    async update(id, name, code = '') {
        const data = await apiCall(`/subjects/${id}/`, 'PUT', { name, code });
        return data.subject;
    },
    
    async delete(id) {
        return await apiCall(`/subjects/${id}/`, 'DELETE');
    }
};

// Lectures API
const LecturesAPI = {
    async getAll(day = null) {
        const query = day ? `?day=${day}` : '';
        const data = await apiCall(`/lectures/${query}`);
        return data.lectures;
    },
    
    async create(subjectId, day, time) {
        const data = await apiCall('/lectures/', 'POST', { 
            subject_id: subjectId, 
            day: day.toLowerCase(), 
            time 
        });
        return data.lecture;
    },
    
    async delete(id) {
        return await apiCall(`/lectures/${id}/`, 'DELETE');
    }
};

// Attendance Records API
const RecordsAPI = {
    async getAll(date = null) {
        const query = date ? `?date=${date}` : '';
        const data = await apiCall(`/records/${query}`);
        return data.records;
    },
    
    async mark(subjectId, date, status, lectureTime = null) {
        const body = { subject_id: subjectId, date, status };
        if (lectureTime) body.lecture_time = lectureTime;
        const data = await apiCall('/records/', 'POST', body);
        return data.record;
    },
    
    async delete(id) {
        return await apiCall(`/records/${id}/`, 'DELETE');
    }
};

// Settings API
const SettingsAPI = {
    async get() {
        const data = await apiCall('/settings/');
        return data.target_percentage;
    },
    
    async update(targetPercentage) {
        const data = await apiCall('/settings/', 'PUT', { target_percentage: targetPercentage });
        return data.target_percentage;
    }
};

// Dashboard API
const DashboardAPI = {
    async getSummary() {
        return await apiCall('/dashboard/summary/');
    }
};

// Data Transformation Helpers
const DataTransform = {
    // Convert API subjects to frontend format
    subjectsToFrontend(apiSubjects, apiRecords) {
        return apiSubjects.map(sub => {
            const records = apiRecords.filter(r => r.subject_id === sub.id);
            const dates = {};
            let att = 0, miss = 0;
            
            records.forEach(r => {
                // Parse date correctly to avoid timezone issues
                const [year, month, day] = r.date.split('-').map(Number);
                const key = new Date(year, month - 1, day).toDateString();
                // Convert API status to frontend format
                if (r.status === 'present') {
                    dates[key] = 'att';
                    att++;
                } else if (r.status === 'absent') {
                    dates[key] = 'miss';
                    miss++;
                } else if (r.status === 'off') {
                    dates[key] = 'off';
                }
            });
            
            return {
                id: sub.id,
                name: sub.name,
                code: sub.code || '',
                att,
                miss,
                dates
            };
        });
    },
    
    // Convert API lectures to frontend timetable format
    lecturesToTimetable(apiLectures, apiSubjects) {
        const days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];
        const tt = [[], [], [], [], [], [], []];
        
        apiLectures.forEach(lec => {
            const dayIndex = days.indexOf(lec.day.toLowerCase());
            if (dayIndex !== -1) {
                const subject = apiSubjects.find(s => s.id === lec.subject_id);
                if (subject) {
                    tt[dayIndex].push({
                        id: lec.id,
                        name: subject.name,
                        subjectId: subject.id,
                        time: lec.time
                    });
                }
            }
        });
        
        return tt;
    },
    
    // Convert frontend date to API format (YYYY-MM-DD)
    dateToAPI(dateStr) {
        // Parse the date string correctly to avoid timezone issues
        const d = new Date(dateStr);
        const year = d.getFullYear();
        const month = String(d.getMonth() + 1).padStart(2, '0');
        const day = String(d.getDate()).padStart(2, '0');
        return `${year}-${month}-${day}`;
    },
    
    // Convert 12-hour time to 24-hour format for API
    timeTo24Hour(time12) {
        if (!time12 || time12 === 'Time not set') return null;
        const [time, period] = time12.split(' ');
        let [hours, minutes] = time.split(':');
        hours = parseInt(hours);
        
        if (period === 'PM' && hours !== 12) hours += 12;
        if (period === 'AM' && hours === 12) hours = 0;
        
        return `${hours.toString().padStart(2, '0')}:${minutes}`;
    },
    
    // Convert 24-hour time to 12-hour format for frontend
    timeTo12Hour(time24) {
        if (!time24) return 'Time not set';
        const [hours, minutes] = time24.split(':');
        let h = parseInt(hours);
        const period = h >= 12 ? 'PM' : 'AM';
        h = h % 12 || 12;
        return `${h}:${minutes} ${period}`;
    }
};

// Export for use in main app
window.AttendanceAPI = {
    Auth: AuthAPI,
    Subjects: SubjectsAPI,
    Lectures: LecturesAPI,
    Records: RecordsAPI,
    Settings: SettingsAPI,
    Dashboard: DashboardAPI,
    Transform: DataTransform
};
