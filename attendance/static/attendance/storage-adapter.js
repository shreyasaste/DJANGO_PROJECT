// Storage Adapter - Bridges localStorage code to API
// This allows your existing code to work with minimal changes

class APIStorage {
    constructor() {
        this.cache = {
            subjects: [],
            lectures: [],
            records: [],
            target: 80,
            user: null
        };
        this.initialized = false;
    }
    
    async init(force = false) {
        if (this.initialized && !force) return;
        
        try {
            // Load all data from API
            const [subjects, lectures, records, target, user] = await Promise.all([
                AttendanceAPI.Subjects.getAll(),
                AttendanceAPI.Lectures.getAll(),
                AttendanceAPI.Records.getAll(),
                AttendanceAPI.Settings.get(),
                AttendanceAPI.Auth.getMe()
            ]);
            
            this.cache.subjects = subjects;
            this.cache.lectures = lectures;
            this.cache.records = records;
            this.cache.target = target;
            this.cache.user = user.user;
            this.initialized = true;
        } catch (err) {
            console.error('Failed to initialize API storage:', err);
            throw err;
        }
    }
    
    // Get subjects in frontend format
    getSubjects() {
        return AttendanceAPI.Transform.subjectsToFrontend(
            this.cache.subjects,
            this.cache.records
        );
    }
    
    // Get timetable in frontend format
    getTimetable() {
        return AttendanceAPI.Transform.lecturesToTimetable(
            this.cache.lectures,
            this.cache.subjects
        );
    }
    
    // Add subject
    async addSubject(name, code = '') {
        const newSubject = await AttendanceAPI.Subjects.create(name, code);
        this.cache.subjects.push(newSubject);
        return newSubject;
    }
    
    // Delete subject
    async deleteSubject(subjectId) {
        await AttendanceAPI.Subjects.delete(subjectId);
        this.cache.subjects = this.cache.subjects.filter(s => s.id !== subjectId);
        this.cache.lectures = this.cache.lectures.filter(l => l.subject_id !== subjectId);
        this.cache.records = this.cache.records.filter(r => r.subject_id !== subjectId);
    }
    
    // Mark attendance
    async markAttendance(subjectId, dateStr, status) {
        const apiDate = AttendanceAPI.Transform.dateToAPI(dateStr);
        
        // Check if record exists for this date
        const existing = this.cache.records.find(
            r => r.subject_id === subjectId && r.date === apiDate
        );
        
        if (status === 'clear') {
            // Delete record
            if (existing) {
                await AttendanceAPI.Records.delete(existing.id);
                this.cache.records = this.cache.records.filter(r => r.id !== existing.id);
            }
        } else {
            // Create or update record
            const apiStatus = status === 'att' ? 'present' : (status === 'miss' ? 'absent' : 'off');
            const record = await AttendanceAPI.Records.mark(subjectId, apiDate, apiStatus);
            
            if (existing) {
                // Update existing in cache
                const index = this.cache.records.findIndex(r => r.id === existing.id);
                this.cache.records[index] = record;
            } else {
                // Add new to cache
                this.cache.records.push(record);
            }
        }
        
        // Force refresh to update UI
        await this.init(true);
    }
    
    // Add lecture to timetable
    async addLecture(dayIndex, subjectName, time) {
        const days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];
        const subject = this.cache.subjects.find(s => s.name === subjectName);
        
        if (!subject) throw new Error('Subject not found');
        
        const apiTime = AttendanceAPI.Transform.timeTo24Hour(time);
        const lecture = await AttendanceAPI.Lectures.create(subject.id, days[dayIndex], apiTime);
        this.cache.lectures.push(lecture);
        return lecture;
    }
    
    // Delete lecture
    async deleteLecture(lectureId) {
        await AttendanceAPI.Lectures.delete(lectureId);
        this.cache.lectures = this.cache.lectures.filter(l => l.id !== lectureId);
    }
    
    // Update lecture time
    async updateLectureTime(lectureId, newTime) {
        // Note: API doesn't have update endpoint, so delete and recreate
        const lecture = this.cache.lectures.find(l => l.id === lectureId);
        if (!lecture) return;
        
        await this.deleteLecture(lectureId);
        const apiTime = AttendanceAPI.Transform.timeTo24Hour(newTime);
        const newLecture = await AttendanceAPI.Lectures.create(
            lecture.subject_id,
            lecture.day,
            apiTime
        );
        this.cache.lectures.push(newLecture);
    }
    
    // Update target percentage
    async updateTarget(target) {
        await AttendanceAPI.Settings.update(target);
        this.cache.target = target;
    }
    
    getTarget() {
        return this.cache.target;
    }
    
    getUser() {
        return this.cache.user;
    }
}

// Create global instance
window.apiStorage = new APIStorage();
