# RollCall Technical Design Document

## 1. Project Overview

RollCall is a Flask-based web application for class scheduling and student attendance reporting.

The system uses:

- Python for application logic
- Flask for web routing
- SQLite for data storage
- HTML and CSS for the user interface
- Requests for API communication
- Pytest for automated testing
- Git and GitHub for version control

## 2. System Architecture

RollCall follows a lightweight Model-View-Controller architecture.

The architecture contains:

- Model
- View
- Controller
- External API Service

The overall structure is:

    User
      ↓
    Flask Routes
      ↓
    Database and API Services
      ↓
    HTML Templates and System Response

## 3. Architecture Components

### Model

The Model represents system data and database operations.

The main Model component is:

    database.py

The Model is responsible for:

- Opening SQLite connections
- Creating database tables
- Enabling foreign-key support
- Saving records
- Retrieving records
- Updating records
- Deleting records

### View

The View represents the user interface.

The View components are stored in:

    templates/

The main templates include:

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

The stylesheet is stored in:

    static/style.css

### Controller

The Controller is implemented through Flask routes in:

    app.py

The Controller is responsible for:

- Receiving browser requests
- Validating form data
- Calling database functions
- Calling the holiday API service
- Returning HTML templates
- Displaying success or error messages

### External API Service

The external API logic is separated into:

    holiday_service.py

This service checks whether a selected date is a Philippine public holiday.

## 4. Project Structure

    RollCall/
    ├── app.py
    ├── database.py
    ├── holiday_service.py
    ├── requirements.txt
    ├── README.md
    ├── .gitignore
    ├── templates/
    │   ├── base.html
    │   ├── home.html
    │   ├── students.html
    │   ├── student_form.html
    │   ├── classes.html
    │   ├── class_form.html
    │   ├── class_edit_form.html
    │   ├── enrollment.html
    │   ├── attendance.html
    │   └── reports.html
    ├── static/
    │   └── style.css
    ├── tests/
    │   └── test_app.py
    ├── docs/
    └── screenshots/

## 5. Database Design

RollCall uses SQLite for local data storage.

The database file is:

    rollcall.db

The database is created automatically when the application starts.

## 6. Database Tables

### Students Table

Stores student information.

Fields:

| Field          | Type    | Description            |
| -------------- | ------- | ---------------------- |
| id             | INTEGER | Primary key            |
| student_number | TEXT    | Unique student number  |
| full_name      | TEXT    | Student’s full name    |
| email          | TEXT    | Optional student email |
| created_at     | TEXT    | Record creation date   |

### Classes Table

Stores teacher class schedules.

Fields:

| Field        | Type    | Description             |
| ------------ | ------- | ----------------------- |
| id           | INTEGER | Primary key             |
| subject_code | TEXT    | Subject code            |
| subject_name | TEXT    | Subject name            |
| section      | TEXT    | Class section           |
| room         | TEXT    | Classroom or laboratory |
| meeting_day  | TEXT    | Day of the class        |
| start_time   | TEXT    | Class start time        |
| end_time     | TEXT    | Class end time          |
| created_at   | TEXT    | Record creation date    |

### Enrollments Table

Connects students with classes.

Fields:

| Field      | Type    | Description                      |
| ---------- | ------- | -------------------------------- |
| class_id   | INTEGER | Foreign key referencing classes  |
| student_id | INTEGER | Foreign key referencing students |

The combination of class ID and student ID is unique to prevent duplicate enrollment.

### Attendance Table

Stores daily attendance.

Fields:

| Field           | Type    | Description                       |
| --------------- | ------- | --------------------------------- |
| id              | INTEGER | Primary key                       |
| class_id        | INTEGER | Foreign key referencing classes   |
| student_id      | INTEGER | Foreign key referencing students  |
| attendance_date | TEXT    | Date of attendance                |
| status          | TEXT    | Present, Absent, Late, or Excused |

The combination of class ID, student ID, and attendance date is unique. This prevents duplicate attendance entries for the same student, class, and date.

## 7. Database Relationships

The relationships are:

    Students 1 ────< Enrollments >──── 1 Classes

    Students 1 ────< Attendance >──── 1 Classes

A student can enroll in multiple classes.

A class can contain multiple students.

A student can have multiple attendance records.

## 8. Main Application Routes

| Route                                        | Method    | Purpose                     |
| -------------------------------------------- | --------- | --------------------------- |
| `/`                                          | GET       | Displays the dashboard      |
| `/students`                                  | GET       | Displays students           |
| `/students/new`                              | GET, POST | Adds a student              |
| `/students/<id>/edit`                        | GET, POST | Edits a student             |
| `/students/<id>/delete`                      | POST      | Deletes a student           |
| `/classes`                                   | GET       | Displays class schedules    |
| `/classes/new`                               | GET, POST | Adds a class                |
| `/classes/<id>/edit`                         | GET, POST | Edits a class               |
| `/classes/<id>/delete`                       | POST      | Deletes a class             |
| `/classes/<id>/students`                     | GET, POST | Manages enrollment          |
| `/classes/<id>/students/<student_id>/remove` | POST      | Removes enrollment          |
| `/classes/<id>/attendance`                   | GET, POST | Records attendance          |
| `/reports`                                   | GET       | Displays attendance reports |

## 9. Attendance Processing Flow

The attendance process works as follows:

1. The teacher selects a class.
2. The teacher selects an attendance date.
3. The system requests holiday information from the external API.
4. The system checks whether the date is a public holiday.
5. If it is a holiday, attendance saving is disabled.
6. If it is not a holiday, enrolled students are displayed.
7. The teacher selects an attendance status.
8. The system validates the status.
9. The attendance record is inserted or updated.
10. The system displays a confirmation message.

## 10. API Integration Design

The API service is located in:

    holiday_service.py

The main function is:

    check_public_holiday(attendance_date)

The function performs these actions:

1. Extracts the year from the selected date.
2. Builds the API URL.
3. Sends a GET request.
4. Applies a timeout.
5. Processes the JSON response.
6. Searches for a matching date.
7. Returns holiday information or an error.

API endpoint:

    https://nagerholidays.com/api/v4/Holidays/PH/{year}

## 11. MVC Design Pattern

RollCall uses a lightweight Model-View-Controller structure.

### Model

The Model consists of:

- database.py
- SQLite tables
- Database queries
- Student, class, enrollment, and attendance records

### View

The View consists of:

- HTML templates
- Navigation layout
- Forms
- Tables
- CSS styling
- Error and success messages

### Controller

The Controller consists of:

- Flask routes in app.py
- Form processing
- Input validation
- Database calls
- API calls
- Template rendering

## 12. Input Validation

The system validates:

- Required student number
- Required student name
- Duplicate student numbers
- Required subject code
- Required subject name
- Required class section
- Required meeting day
- Required start and end times
- End time after start time
- Valid attendance statuses
- Duplicate enrollment records

## 13. Error Handling

The application handles:

- Missing required fields
- Duplicate student numbers
- Invalid class times
- Invalid attendance statuses
- Missing class records
- Missing student records
- Public holiday API errors
- Network failures
- Invalid API responses

The application displays understandable error messages instead of terminating unexpectedly.

## 14. Security Design

The system uses the following basic security practices:

- SQL parameters are used instead of directly joining user input into queries.
- API URLs are fixed inside the application.
- Private student information is not sent to the holiday API.
- The local database file is excluded from Git.
- API credentials are not stored in the source code.
- Delete actions require confirmation in the interface.

## 15. Testing Design

Automated tests are stored in:

    tests/test_app.py

The tests use:

- Pytest
- Flask test client
- Temporary SQLite databases
- Mocked API responses

The tests cover:

- Dashboard loading
- Student creation
- Required-field validation
- Duplicate students
- Student editing
- Student deletion
- Class creation
- Invalid class times
- Holiday API success
- Holiday API failure
- Attendance recording
- Attendance reports
- Holiday attendance restriction

## 16. Deployment and Execution

The application is intended for local execution.

Installation process:

    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    python app.py

The application is accessed through:

    http://127.0.0.1:5000

## 17. Design Limitations

The current design has the following limitations:

- Authentication is not included.
- The application is designed for a single-teacher environment.
- The database is local rather than hosted.
- Public holiday information depends on an external service.
- School-specific suspensions are not automatically available.
- Reports are displayed in HTML and are not exported to PDF.

## 18. Future Technical Improvements

Possible improvements include:

- Separate repository classes for database operations
- Teacher authentication
- Role-based permissions
- Cloud database support
- PDF report generation
- CSV report generation
- School-specific academic calendar support
- Dashboard graphs
- Automated database backups

## 19. Conclusion

The technical design of RollCall separates the application into database, controller, view, and external API components.

The MVC structure supports organization and maintainability. SQLite provides local data storage, while the public holiday API supplies external calendar information. Automated tests verify important system behavior and help reduce the risk of regression errors.
