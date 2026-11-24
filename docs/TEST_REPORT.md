# RollCall Testing and Quality Report

## 1. Purpose

This document records the testing activities performed for RollCall.

The purpose of testing is to verify that the system:

- Accepts valid information.
- Rejects invalid information.
- Saves student records correctly.
- Saves class schedules correctly.
- Records attendance correctly.
- Generates attendance reports.
- Handles duplicate records.
- Handles public holiday API errors.
- Prevents attendance on public holidays.

## 2. Testing Tools

The following tools were used:

- Python
- Pytest
- Flask test client
- SQLite test database
- VS Code
- Mocked API responses

The tests are located in:

    tests/test_app.py

## 3. Testing Approach

Automated tests were used to test the main application functions.

A temporary database is created for every test so that:

- Test data does not affect the real database.
- Each test starts with a clean database.
- Tests can be repeated consistently.
- Student and attendance data can be tested safely.

The public holiday API is tested using mocked responses. This prevents the tests from depending on an internet connection or the actual API server.

## 4. Test Cases

### Test Case 1: Load the Home Page

Description:

Verify that the RollCall dashboard loads correctly.

Test procedure:

1. Send a request to the home page.
2. Check the response status.
3. Check that the RollCall title is displayed.

Expected result:

The dashboard loads successfully and displays RollCall.

Actual result:

The dashboard loaded successfully and displayed RollCall.

Status:

Passed

## Test Case 2: Add a Student

Description:

Verify that a valid student record can be added.

Test procedure:

1. Submit a valid student number.
2. Submit a student name.
3. Submit an email address.
4. Open the student list.

Expected result:

The student is saved and displayed in the student list.

Actual result:

The student was saved and displayed in the student list.

Status:

Passed

## Test Case 3: Validate Required Student Fields

Description:

Verify that a student cannot be added without a student number and name.

Test procedure:

1. Submit an empty student number.
2. Submit an empty student name.
3. Submit the form.

Expected result:

The system rejects the submission and displays a validation message.

Actual result:

The system rejected the submission and displayed a validation message.

Status:

Passed

## Test Case 4: Reject Duplicate Student Numbers

Description:

Verify that duplicate student numbers cannot be added.

Test procedure:

1. Add a student with a student number.
2. Attempt to add another student using the same student number.
3. Submit the form.

Expected result:

The system rejects the duplicate record.

Actual result:

The system rejected the duplicate student number and displayed an error message.

Status:

Passed

## Test Case 5: Edit a Student

Description:

Verify that an existing student record can be updated.

Test procedure:

1. Add a student.
2. Open the edit page.
3. Change the student name and email.
4. Save the changes.

Expected result:

The updated student information is displayed.

Actual result:

The student information was updated successfully.

Status:

Passed

## Test Case 6: Delete a Student

Description:

Verify that a student record can be deleted.

Test procedure:

1. Add a student.
2. Select the delete option.
3. Confirm the deletion.
4. View the student list.

Expected result:

The student is removed from the student list.

Actual result:

The student was removed successfully.

Status:

Passed

## Test Case 7: Add a Class Schedule

Description:

Verify that a valid class schedule can be added.

Test procedure:

1. Enter a subject code.
2. Enter a subject name.
3. Enter a section.
4. Enter a room.
5. Select a meeting day.
6. Enter valid start and end times.
7. Save the schedule.

Expected result:

The class schedule is saved and displayed.

Actual result:

The class schedule was saved and displayed successfully.

Status:

Passed

## Test Case 8: Reject Invalid Class Times

Description:

Verify that the system rejects a class schedule when the end time is earlier than the start time.

Test procedure:

1. Enter a valid class schedule.
2. Enter a start time of 10:00.
3. Enter an end time of 08:00.
4. Submit the form.

Expected result:

The system rejects the schedule and displays an error message.

Actual result:

The system rejected the schedule and displayed the correct error message.

Status:

Passed

## Test Case 9: Find a Public Holiday

Description:

Verify that the public holiday service can identify a holiday.

Test procedure:

1. Provide a sample holiday API response.
2. Check a date included in the response.
3. Process the response.

Expected result:

The system identifies the holiday and returns its name.

Actual result:

The system identified the holiday correctly.

Status:

Passed

## Test Case 10: Handle a Holiday API Network Error

Description:

Verify that the system handles an unavailable API.

Test procedure:

1. Simulate a network error.
2. Call the holiday service.
3. Check the returned result.

Expected result:

The system returns an error message instead of crashing.

Actual result:

The system returned an error message without crashing.

Status:

Passed

## Test Case 11: Record Attendance and Generate a Report

Description:

Verify that attendance can be recorded and included in a report.

Test procedure:

1. Add a student.
2. Add a class.
3. Enroll the student in the class.
4. Record the student as Present.
5. Open the attendance report.

Expected result:

The attendance record is saved and the report displays a 100 percent attendance result.

Actual result:

The attendance record was saved and the report displayed the correct attendance percentage.

Status:

Passed

## Test Case 12: Prevent Attendance on a Public Holiday

Description:

Verify that attendance cannot be saved on a public holiday.

Test procedure:

1. Add a student.
2. Add a class.
3. Enroll the student.
4. Simulate a public holiday response.
5. Attempt to record attendance on that date.

Expected result:

The system prevents the attendance record from being saved.

Actual result:

The system prevented attendance from being saved and displayed a warning message.

Status:

Passed

## 5. Automated Test Result

The automated test suite was executed using:

    pytest

Total test cases:

    12

Passed tests:

    12

Failed tests:

    0

Overall result:

    All automated tests passed.

## 6. Defects Found and Resolved

### Defect 1: Saved attendance status was not displayed

Problem:

After attendance was saved, the page displayed Present as the default option instead of showing the saved status.

Resolution:

The attendance template was updated to compare the stored attendance status with each available option.

Result:

Saved attendance statuses are now displayed correctly when the date is loaded again.

### Defect 2: Jinja template syntax error

Problem:

The attendance template produced a Jinja2 TemplateSyntaxError because of an invalid template expression.

Resolution:

The template logic was simplified and the invalid expression was removed.

Result:

The attendance page loads successfully.

### Defect 3: Test module could not find database.py

Problem:

Pytest could not find the database module during test collection.

Resolution:

The project folder was added to the Python import path in the test file.

Result:

The test module loads successfully and the tests run correctly.

## 7. Quality Assessment

The current RollCall version satisfies the main functional requirements.

The system can:

- Manage students.
- Manage class schedules.
- Enroll students.
- Record attendance.
- Check public holidays.
- Generate attendance reports.
- Validate user input.
- Handle API errors.
- Run automated tests.

The system is suitable for demonstration and further documentation.

## 8. Current Limitations

The system still has the following limitations:

- It does not yet include teacher login.
- It is designed for a single teacher environment.
- Reports cannot currently be exported as PDF files.
- The system requires internet access for live holiday checking.
- The public holiday API does not contain school-specific suspensions.
- More security features may be needed before real-world deployment.

## 9. Future Improvements

Possible future improvements include:

- Add teacher authentication.
- Add role-based access control.
- Add PDF report generation.
- Add CSV report export.
- Add class attendance graphs.
- Add school-specific academic calendars.
- Add database backup and restore.
- Add stronger security controls.

## 10. Conclusion

Testing confirmed that the main RollCall features work as expected.

The automated test suite successfully tested student management, class schedule validation, API behavior, attendance recording, report generation, and holiday restrictions.

The project is ready for final documentation, screenshots, and demonstration preparation.
