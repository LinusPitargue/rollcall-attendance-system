# RollCall

RollCall is a teacher-based class scheduling and student attendance reporting system.

The system allows a teacher to manage student records, create class schedules, enroll students, record attendance, and view attendance reports. It also connects to an external public holiday API to check whether attendance should be recorded on a selected date.

## Project Objectives

RollCall aims to:

- Organize student records
- Manage class schedules
- Enroll students in classes
- Record daily attendance
- Prevent attendance recording on public holidays
- Generate attendance summaries
- Demonstrate database management, API integration, testing, and Git workflow

## Main Features

### Student Management

- Add student records
- View student records
- Edit student information
- Delete student records
- Reject duplicate student numbers

### Class Schedule Management

- Add class schedules
- View class schedules
- Edit class schedules
- Delete class schedules
- Store subject, section, room, day, and time information

### Enrollment Management

- Enroll students into classes
- View enrolled students
- Remove students from classes

### Attendance Management

- Select an attendance date
- Mark students as Present, Absent, Late, or Excused
- Update existing attendance records
- Prevent attendance recording on public holidays

### Attendance Reports

- View attendance records
- Filter reports by class
- Count present, absent, late, and excused records
- Calculate attendance percentages

## External API

RollCall uses the Nager.Date public holiday API to check Philippine public holidays.

Endpoint format:

```text
https://nagerholidays.com/api/v4/Holidays/PH/{year}
```
