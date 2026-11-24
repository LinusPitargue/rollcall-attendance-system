# RollCall User Manual

## 1. Introduction

RollCall is a class scheduling and student attendance reporting system.

The system allows teachers to:

- Manage student records
- Create class schedules
- Enroll students in classes
- Record daily attendance
- Check public holidays
- View attendance reports

## 2. System Requirements

The user needs:

- Python 3.10 or newer
- A web browser
- Internet connection for public holiday checking
- RollCall project files
- Required Python packages

## 3. Installation

Open the RollCall project folder in Visual Studio Code.

Open the VS Code terminal and create a virtual environment:

    python -m venv .venv

Activate the environment using Windows PowerShell:

    .venv\Scripts\Activate.ps1

Install the required packages:

    pip install -r requirements.txt

## 4. Starting the Application

Start the Flask application using:

    python app.py

Open a web browser and go to:

    http://127.0.0.1:5000

The RollCall dashboard should appear.

To stop the application, return to the terminal and press:

    CTRL + C

## 5. Dashboard

### Purpose

The dashboard provides access to the main RollCall functions.

### Procedure

1. Start the application.
2. Open a browser.
3. Go to:

   http://127.0.0.1:5000

4. Use the navigation buttons to access students, classes, and reports.

### Expected Result

The dashboard displays links to:

- Student management
- Class schedules
- Attendance reports

### Screenshot

    screenshots/01-dashboard.png

## 6. Student Management

### Purpose

The Student Management feature allows the teacher to add, view, edit, and delete student records.

### Add a Student

1. Open the dashboard.
2. Select Students.
3. Click Add New Student.
4. Enter the student number.
5. Enter the student’s full name.
6. Enter the email address if available.
7. Click Save Student.

### Expected Result

The student appears in the student database table.

### Edit a Student

1. Open the Students page.
2. Select Edit beside a student.
3. Change the required information.
4. Click Save Student.

### Expected Result

The updated student information appears in the student table.

### Delete a Student

1. Open the Students page.
2. Select Delete beside a student.
3. Confirm the deletion.

### Expected Result

The student is removed from the student list.

### Screenshot

    screenshots/02-students.png

### Troubleshooting

If a duplicate student number is entered, the system displays an error message. Each student must have a unique student number.

## 7. Class Schedule Management

### Purpose

The Class Schedule feature allows the teacher to create and manage class schedules.

### Add a Class Schedule

1. Open the Classes page.
2. Click Add Class Schedule.
3. Enter the subject code.
4. Enter the subject name.
5. Enter the class section.
6. Enter the room.
7. Select the meeting day.
8. Enter the start time.
9. Enter the end time.
10. Click Save Class Schedule.

### Expected Result

The new class appears in the class schedule table.

### Edit a Class Schedule

1. Open the Classes page.
2. Select Edit beside a class.
3. Change the schedule information.
4. Click Update Class Schedule.

### Expected Result

The updated class information appears in the class schedule table.

### Delete a Class Schedule

1. Open the Classes page.
2. Select Delete beside a class.
3. Confirm the deletion.

### Expected Result

The class schedule is removed.

### Screenshot

    screenshots/03-class-schedule.png

### Troubleshooting

The end time must be later than the start time. The system rejects schedules with invalid time ranges.

## 8. Student Enrollment

### Purpose

The Enrollment feature connects students to their assigned classes.

### Enroll a Student

1. Open the Classes page.
2. Select Students beside a class.
3. Choose a student from the enrollment list.
4. Click Enroll Student.

### Expected Result

The student appears in the enrolled students table.

### Remove an Enrollment

1. Open the enrolled students page.
2. Select Remove beside a student.
3. Confirm the removal.

### Expected Result

The student is removed from that class but remains in the main student database.

### Screenshot

    screenshots/04-enrollment.png

## 9. Recording Attendance

### Purpose

The Attendance feature allows the teacher to record attendance for enrolled students.

### Procedure

1. Open the Classes page.
2. Select Attendance beside a class.
3. Choose an attendance date.
4. Click Check Date.
5. Select a status for each student:
   - Present
   - Absent
   - Late
   - Excused
6. Click Save Attendance.

### Expected Result

The attendance records are saved for the selected class and date.

### Updating Attendance

1. Open the same class and attendance date.
2. Change the student’s status.
3. Click Save Attendance again.

### Expected Result

The existing attendance record is updated instead of creating a duplicate record.

### Screenshot

    screenshots/05-attendance.png

## 10. Public Holiday Validation

### Purpose

RollCall uses an external public holiday API to check whether the selected attendance date is a Philippine public holiday.

### Procedure

1. Open the Attendance page.
2. Select an attendance date.
3. Click Check Date.
4. Wait for the system to check the public holiday API.

### Expected Result

If the date is not a public holiday, attendance can be saved.

If the date is a public holiday, the system displays a warning and disables attendance saving.

### Screenshot

    screenshots/06-holiday-warning.png

### Troubleshooting

If the API cannot be reached, the system displays a warning message. Check the internet connection and verify the date manually.

## 11. Attendance Reports

### Purpose

The Reports feature summarizes student attendance.

The report displays:

- Class
- Student number
- Student name
- Total attendance records
- Present count
- Absent count
- Late count
- Excused count
- Attendance percentage

### Procedure

1. Open the Reports page.
2. Select All Classes or choose a specific class.
3. Click Filter Report.

### Expected Result

The system displays attendance totals and calculates the attendance percentage.

### Screenshot

    screenshots/07-reports.png

## 12. Database Information

RollCall automatically creates a SQLite database named:

    rollcall.db

The database contains the following tables:

- students
- classes
- enrollments
- attendance

The database is created when the application is first started.

## 13. Resetting the Database

To reset the system:

1. Stop the Flask application.
2. Delete the file:

   rollcall.db

3. Start the application again:

   python app.py

A new empty database will be created.

Warning: Resetting the database permanently removes the current student, class, enrollment, and attendance records.

## 14. Common Problems

### The application does not start

Check that the virtual environment is active:

    .venv\Scripts\Activate.ps1

Then install the dependencies:

    pip install -r requirements.txt

### The browser cannot open the system

Make sure the Flask application is running and open:

    http://127.0.0.1:5000

### The port is already in use

Stop the previous Flask process by pressing:

    CTRL + C

Then run the application again.

### Attendance cannot be saved

Check whether the selected date is a public holiday. Also confirm that students have been enrolled in the class.

### The report is empty

Record attendance for at least one enrolled student before opening the Reports page.

## 15. Security and Privacy Notes

The system stores student information in a local SQLite database.

The application does not send student names, student numbers, or attendance records to the public holiday API.

Only the selected attendance year is sent to the API.

The database file is excluded from Git using the .gitignore file.

## 16. Conclusion

RollCall provides a centralized way to manage class schedules, student records, enrollment, attendance, and attendance reports.

The user manual provides the installation, execution, usage, and troubleshooting procedures required to operate the application.
