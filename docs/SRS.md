# RollCall Software Requirements Specification

## 1. Project Information

Project Title:

RollCall: A Class Scheduling and Student Attendance Reporting System

Programming Language:

Python

Framework:

Flask

Database:

SQLite

External API:

Nager.Date Public Holiday API

Design Pattern:

Model-View-Controller (MVC)

## 2. System Description

RollCall is a web-based attendance management system designed for teachers.

The system allows teachers to manage student records, create class schedules, enroll students in classes, record attendance, and generate attendance reports.

The system also uses an external public holiday API to determine whether an attendance date is a Philippine public holiday. Attendance cannot be recorded on dates identified as public holidays.

## 3. Problem Statement

Teachers may record attendance using paper forms or separate spreadsheets. These methods can make attendance records difficult to organize, update, calculate, and retrieve.

Manual processes can also cause:

- Duplicate student records
- Incorrect attendance calculations
- Lost or incomplete attendance information
- Difficulty finding previous attendance records
- Attendance being recorded on public holidays
- Time-consuming report preparation

RollCall addresses these problems by providing a centralized system for managing class schedules, student records, attendance data, and reports.

## 4. Target Users

### Primary User

The primary user is a teacher who manages classes and records student attendance.

### Secondary Users

Possible secondary users include:

- School administrators
- Academic coordinators
- Authorized staff members

The current version focuses mainly on teacher functionality.

## 5. Project Objectives

RollCall aims to:

1. Provide a centralized student database.
2. Allow teachers to create and manage class schedules.
3. Allow students to be assigned to classes.
4. Allow teachers to record daily attendance.
5. Support Present, Absent, Late, and Excused attendance statuses.
6. Automatically calculate attendance percentages.
7. Generate attendance summaries by class and student.
8. Check public holidays through an external API.
9. Validate user input.
10. Handle API and database errors.
11. Demonstrate Git, GitHub, testing, documentation, and software design practices.

## 6. Project Scope

### Included Features

The system includes:

- Student record management
- Student number validation
- Class schedule management
- Student enrollment
- Attendance recording
- Attendance status updates
- Public holiday checking
- Attendance percentage calculation
- Attendance reports
- Input validation
- API error handling
- SQLite database storage
- Automated tests
- GitHub version control

### Excluded Features

The system does not include:

- Facial recognition
- Biometric scanning
- Parent accounts
- Student mobile applications
- Payroll management
- Online grading
- Automatic location tracking
- Multiple-school administration
- PDF report exporting
- Teacher authentication in the current version

## 7. Functional Requirements

### FR-01: Student Creation

The system shall allow the teacher to add a student using a student number, full name, and optional email address.

Acceptance Criteria:

- The teacher can submit valid student information.
- The student is stored in the database.
- The student appears in the student list.

### FR-02: Student Validation

The system shall validate required student information.

Acceptance Criteria:

- A student number is required.
- A full name is required.
- Duplicate student numbers are rejected.
- An understandable error message is displayed.

### FR-03: Student Editing

The system shall allow the teacher to edit an existing student record.

Acceptance Criteria:

- The teacher can open an existing student.
- The teacher can change the student information.
- The updated information is stored and displayed.

### FR-04: Student Deletion

The system shall allow the teacher to delete a student record.

Acceptance Criteria:

- The teacher must confirm the deletion.
- The student record is removed from the student list.

### FR-05: Class Schedule Creation

The system shall allow the teacher to create a class schedule.

The class schedule shall include:

- Subject code
- Subject name
- Section
- Room
- Meeting day
- Start time
- End time

Acceptance Criteria:

- Required fields must be completed.
- The end time must be later than the start time.
- The class schedule appears in the class list after saving.

### FR-06: Class Schedule Editing

The system shall allow the teacher to edit an existing class schedule.

Acceptance Criteria:

- The teacher can open a class schedule.
- The teacher can modify schedule information.
- The updated schedule is displayed.

### FR-07: Class Schedule Deletion

The system shall allow the teacher to delete a class schedule.

Acceptance Criteria:

- The teacher must confirm the deletion.
- The class schedule is removed.

### FR-08: Student Enrollment

The system shall allow the teacher to enroll students in a class.

Acceptance Criteria:

- Available students are displayed.
- A selected student can be enrolled.
- A student cannot be enrolled twice in the same class.
- Enrolled students are displayed.

### FR-09: Enrollment Removal

The system shall allow the teacher to remove a student from a class.

Acceptance Criteria:

- The teacher can select an enrolled student.
- The enrollment is removed.
- The student remains in the main student database.

### FR-10: Attendance Recording

The system shall allow the teacher to record attendance for enrolled students.

Attendance statuses shall include:

- Present
- Absent
- Late
- Excused

Acceptance Criteria:

- The teacher can select a class.
- The teacher can select an attendance date.
- The teacher can assign a status to each enrolled student.
- The attendance record is saved.

### FR-11: Attendance Updating

The system shall allow existing attendance records to be updated.

Acceptance Criteria:

- The existing status is displayed when the date is loaded.
- The teacher can change the status.
- The updated status replaces the previous status.

### FR-12: Public Holiday Validation

The system shall check the selected attendance date using the public holiday API.

Acceptance Criteria:

- The system sends a request to the API.
- A public holiday is identified when the date matches.
- Attendance saving is disabled on public holidays.
- A warning message is displayed.

### FR-13: API Error Handling

The system shall handle API connection errors.

Acceptance Criteria:

- The system does not crash when the API is unavailable.
- A warning message is displayed.
- The teacher is informed that the date should be checked manually.

### FR-14: Attendance Reports

The system shall generate attendance reports.

Reports shall include:

- Class
- Student number
- Student name
- Total attendance records
- Present count
- Absent count
- Late count
- Excused count
- Attendance percentage

Acceptance Criteria:

- The report displays saved attendance data.
- The attendance percentage is calculated correctly.
- The report can be filtered by class.

## 8. Nonfunctional Requirements

### Usability

The interface shall be understandable and usable by a teacher with basic computer skills.

### Performance

Common system operations should respond within an acceptable time under normal local use.

### Reliability

The system shall display understandable messages when invalid information or errors occur.

### Security

The system shall:

- Validate user input.
- Avoid exposing database errors unnecessarily.
- Avoid sending private student information to the public API.
- Exclude database files and secrets from Git.

### Maintainability

The project shall use:

- Organized folders
- Meaningful file names
- Consistent formatting
- Reusable templates
- Documented functions
- Git version control

### Testability

Core system functions shall have repeatable automated tests using Pytest.

### Portability

The system shall run on a computer with Python, Flask, the required packages, and a supported web browser.

## 9. External API Requirements

The system uses the Nager.Date public holiday API.

Endpoint format:

    https://nagerholidays.com/api/v4/Holidays/PH/{year}

HTTP method:

    GET

The system uses the returned date and holiday name to determine whether attendance should be saved.

## 10. Data Requirements

The system stores the following information.

### Student

- Student ID
- Student number
- Full name
- Email
- Creation date

### Class

- Class ID
- Subject code
- Subject name
- Section
- Room
- Meeting day
- Start time
- End time

### Enrollment

- Class ID
- Student ID

### Attendance

- Attendance ID
- Class ID
- Student ID
- Attendance date
- Attendance status

## 11. Hardware Requirements

Minimum hardware requirements:

- Computer or laptop
- At least 4 GB RAM
- At least 500 MB available storage
- Keyboard and mouse
- Internet connection for API requests

## 12. Software Requirements

Required software:

- Windows, macOS, or Linux
- Python 3.10 or newer
- Visual Studio Code
- Git
- Web browser
- Flask
- Requests
- Pytest

## 13. Constraints

The project has the following constraints:

- The system is designed for local use.
- The system depends on the availability of the public holiday API.
- The current version does not include authentication.
- The public holiday API may not include school-specific suspensions.
- The database is stored locally using SQLite.
- The system is designed for a single-teacher environment.

## 14. Acceptance Criteria

The project will be considered successful when:

1. The application starts successfully.
2. Students can be added, edited, viewed, and deleted.
3. Class schedules can be added, edited, viewed, and deleted.
4. Students can be enrolled in classes.
5. Attendance can be recorded for enrolled students.
6. Attendance records can be updated.
7. Public holidays are checked using the external API.
8. Attendance is blocked on detected public holidays.
9. Attendance reports display correct totals and percentages.
10. Invalid inputs are rejected.
11. API errors are handled.
12. Automated tests pass successfully.
13. The application can be installed using the README instructions.

## 15. Future Improvements

Future versions may include:

- Teacher login and authentication
- Role-based access control
- PDF report generation
- CSV report export
- Graphical attendance charts
- School-specific academic calendars
- Database backup and restore
- Student and parent portals
- Mobile application support

## 16. Conclusion

RollCall provides a centralized solution for class scheduling, student management, attendance recording, and attendance reporting.

The system meets the main project requirements by including a functional web application, SQLite database, external API integration, MVC-style organization, automated testing, GitHub version control, and technical documentation.
