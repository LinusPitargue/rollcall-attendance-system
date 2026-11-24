# RollCall Design Pattern Documentation

## 1. Selected Design Pattern

The selected design pattern for RollCall is the Model-View-Controller (MVC) pattern.

MVC separates the application into three main components:

- Model
- View
- Controller

This separation makes the application easier to organize, test, maintain, and update.

## 2. Why MVC Was Selected

RollCall has different responsibilities that can be separated naturally.

The system needs to:

- Store student, class, enrollment, and attendance data.
- Display pages and forms to the teacher.
- Process requests and control application behavior.

MVC is suitable because it prevents database logic, user-interface code, and request-processing code from being unnecessarily mixed together.

## 3. MVC Components in RollCall

### Model

The Model represents the application data and database operations.

In RollCall, the Model includes:

- database.py
- SQLite database tables
- Student records
- Class schedule records
- Enrollment records
- Attendance records

The database tables are:

- students
- classes
- enrollments
- attendance

The Model is responsible for storing and retrieving information.

### View

The View represents the user interface.

In RollCall, the View includes the HTML files inside the templates folder:

- base.html
- home.html
- students.html
- student_form.html
- classes.html
- class_form.html
- class_edit_form.html
- enrollment.html
- attendance.html
- reports.html

The templates display forms, tables, buttons, error messages, and reports to the teacher.

The shared base.html file provides the common navigation bar and stylesheet connection.

### Controller

The Controller receives user requests and controls the application workflow.

In RollCall, the Controller is implemented through Flask routes in:

    app.py

Examples include:

- /students
- /students/new
- /classes
- /classes/new
- /classes/<class_id>/students
- /classes/<class_id>/attendance
- /reports

The routes receive requests, validate input, communicate with the database, and select the correct View.

## 4. Request Flow

The basic MVC request flow is:

1. The teacher opens a page or submits a form.
2. A Flask route receives the request.
3. The route validates the submitted information.
4. The route reads from or writes to the database.
5. The route sends the result to an HTML template.
6. The template displays the updated information.

Example:

    Teacher submits attendance
            ↓
    Flask attendance route
            ↓
    Database attendance table
            ↓
    Attendance template
            ↓
    Updated attendance page

## 5. Example: Adding a Student

When a teacher adds a student:

1. The teacher opens the student form.
2. The student_form.html View displays the form.
3. The /students/new Controller receives the submitted form.
4. The Controller validates the student number and name.
5. The Model stores the student in the SQLite database.
6. The Controller redirects to the student list.
7. The students.html View displays the new student.

## 6. Example: Recording Attendance

When a teacher records attendance:

1. The teacher selects a class and attendance date.
2. The attendance.html View displays the enrolled students.
3. The attendance route in app.py receives the submitted statuses.
4. The Controller validates the attendance status.
5. The Controller checks the public holiday API.
6. The Model saves the attendance records in SQLite.
7. The View displays a confirmation message or an error message.

## 7. Benefits of MVC in RollCall

### Separation of Responsibilities

Each part of the system has a specific responsibility.

### Easier Maintenance

Changes to the HTML interface can be made without completely rewriting the database structure.

### Improved Testing

Routes and database operations can be tested independently from the visual interface.

### Reduced Code Duplication

Common page structures can be placed in base.html.

### Better Organization

The project files are grouped according to their purpose.

## 8. Comparison with an Alternative

An alternative approach would be placing database queries, HTML output, and request processing inside one large Python file.

That approach would make the system more difficult to maintain because:

- Database changes could affect the interface.
- HTML changes could affect application logic.
- Testing would be more difficult.
- The code would become harder to understand as features increase.

MVC is more suitable because it separates these responsibilities.

## 9. Limitations

The current project uses a lightweight MVC-style structure rather than a large enterprise MVC framework.

Some database queries are still located inside the Flask routes. A future improvement would be to move more database operations into separate repository or model classes.

## 10. Evidence

The following files demonstrate the MVC structure:

| MVC Component         | RollCall Evidence                                |
| --------------------- | ------------------------------------------------ |
| Model                 | database.py, SQLite tables, and database queries |
| View                  | HTML files in the templates folder               |
| Controller            | Flask routes in app.py                           |
| Shared View Structure | templates/base.html                              |
| Testing               | tests/test_app.py                                |

## 11. Conclusion

The MVC pattern is appropriate for RollCall because the system contains database records, user-interface pages, and request-processing logic.

Separating the Model, View, and Controller makes the application more organized, testable, maintainable, and suitable for future improvements.
