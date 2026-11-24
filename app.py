import sqlite3
from datetime import date

from flask import Flask, redirect, render_template, request

from database import get_connection, initialize_database


app = Flask(__name__)


VALID_ATTENDANCE_STATUSES = {
    "Present",
    "Absent",
    "Late",
    "Excused",
}


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>RollCall</title>
    </head>
    <body>
        <h1>RollCall</h1>
        <p>Class scheduling and student attendance reporting system.</p>
        <p>Database connection is ready.</p>

        <p>
            <a href="/students">View Students</a>
        </p>

        <p>
            <a href="/classes">View Class Schedules</a>
        </p>
    </body>
    </html>
    """


@app.route("/students")
def students():
    connection = get_connection()

    student_list = connection.execute(
        """
        SELECT id, student_number, full_name, email
        FROM students
        ORDER BY full_name
        """
    ).fetchall()

    connection.close()

    return render_template("students.html", students=student_list)


@app.route("/students/new", methods=["GET", "POST"])
def new_student():
    error = None

    if request.method == "POST":
        student_number = request.form["student_number"].strip()
        full_name = request.form["full_name"].strip()
        email = request.form["email"].strip()

        if not student_number or not full_name:
            error = "Student number and full name are required."
        else:
            connection = get_connection()

            try:
                connection.execute(
                    """
                    INSERT INTO students
                    (student_number, full_name, email)
                    VALUES (?, ?, ?)
                    """,
                    (student_number, full_name, email),
                )
                connection.commit()
                connection.close()

                return redirect("/students")

            except sqlite3.IntegrityError:
                connection.close()
                error = "That student number already exists."

    return render_template(
        "student_form.html",
        error=error,
        student=None,
        form_title="Add Student",
    )


@app.route("/students/<int:student_id>/edit", methods=["GET", "POST"])
def edit_student(student_id):
    connection = get_connection()

    student = connection.execute(
        """
        SELECT id, student_number, full_name, email
        FROM students
        WHERE id = ?
        """,
        (student_id,),
    ).fetchone()

    if student is None:
        connection.close()
        return "Student not found", 404

    error = None

    if request.method == "POST":
        student_number = request.form["student_number"].strip()
        full_name = request.form["full_name"].strip()
        email = request.form["email"].strip()

        if not student_number or not full_name:
            error = "Student number and full name are required."
        else:
            try:
                connection.execute(
                    """
                    UPDATE students
                    SET student_number = ?,
                        full_name = ?,
                        email = ?
                    WHERE id = ?
                    """,
                    (student_number, full_name, email, student_id),
                )
                connection.commit()
                connection.close()

                return redirect("/students")

            except sqlite3.IntegrityError:
                error = "That student number already exists."

    connection.close()

    return render_template(
        "student_form.html",
        error=error,
        student=student,
        form_title="Edit Student",
    )


@app.route("/students/<int:student_id>/delete", methods=["POST"])
def delete_student(student_id):
    connection = get_connection()

    connection.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,),
    )

    connection.commit()
    connection.close()

    return redirect("/students")


@app.route("/classes")
def classes():
    connection = get_connection()

    class_list = connection.execute(
        """
        SELECT
            classes.id,
            classes.subject_code,
            classes.subject_name,
            classes.section,
            classes.room,
            classes.meeting_day,
            classes.start_time,
            classes.end_time,
            COUNT(enrollments.student_id) AS student_count
        FROM classes
        LEFT JOIN enrollments
            ON classes.id = enrollments.class_id
        GROUP BY classes.id
        ORDER BY classes.subject_code
        """
    ).fetchall()

    connection.close()

    return render_template("classes.html", classes=class_list)


@app.route("/classes/new", methods=["GET", "POST"])
def new_class():
    error = None
    form_data = {}

    if request.method == "POST":
        form_data = request.form

        subject_code = request.form["subject_code"].strip()
        subject_name = request.form["subject_name"].strip()
        section = request.form["section"].strip()
        room = request.form["room"].strip()
        meeting_day = request.form["meeting_day"].strip()
        start_time = request.form["start_time"].strip()
        end_time = request.form["end_time"].strip()

        required_values = [
            subject_code,
            subject_name,
            section,
            meeting_day,
            start_time,
            end_time,
        ]

        if not all(required_values):
            error = "Please complete all required fields."
        elif start_time >= end_time:
            error = "End time must be later than start time."
        else:
            connection = get_connection()

            connection.execute(
                """
                INSERT INTO classes
                (
                    subject_code,
                    subject_name,
                    section,
                    room,
                    meeting_day,
                    start_time,
                    end_time
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    subject_code,
                    subject_name,
                    section,
                    room,
                    meeting_day,
                    start_time,
                    end_time,
                ),
            )

            connection.commit()
            connection.close()

            return redirect("/classes")

    return render_template(
        "class_form.html",
        error=error,
        form_data=form_data,
    )


@app.route("/classes/<int:class_id>/edit", methods=["GET", "POST"])
def edit_class(class_id):
    connection = get_connection()

    class_item = connection.execute(
        """
        SELECT
            id,
            subject_code,
            subject_name,
            section,
            room,
            meeting_day,
            start_time,
            end_time
        FROM classes
        WHERE id = ?
        """,
        (class_id,),
    ).fetchone()

    if class_item is None:
        connection.close()
        return "Class schedule not found", 404

    error = None
    form_data = {}

    if request.method == "POST":
        form_data = request.form

        subject_code = request.form["subject_code"].strip()
        subject_name = request.form["subject_name"].strip()
        section = request.form["section"].strip()
        room = request.form["room"].strip()
        meeting_day = request.form["meeting_day"].strip()
        start_time = request.form["start_time"].strip()
        end_time = request.form["end_time"].strip()

        required_values = [
            subject_code,
            subject_name,
            section,
            meeting_day,
            start_time,
            end_time,
        ]

        if not all(required_values):
            error = "Please complete all required fields."
        elif start_time >= end_time:
            error = "End time must be later than start time."
        else:
            connection.execute(
                """
                UPDATE classes
                SET subject_code = ?,
                    subject_name = ?,
                    section = ?,
                    room = ?,
                    meeting_day = ?,
                    start_time = ?,
                    end_time = ?
                WHERE id = ?
                """,
                (
                    subject_code,
                    subject_name,
                    section,
                    room,
                    meeting_day,
                    start_time,
                    end_time,
                    class_id,
                ),
            )

            connection.commit()
            connection.close()

            return redirect("/classes")

    connection.close()

    return render_template(
        "class_edit_form.html",
        error=error,
        form_data=form_data,
        class_item=class_item,
    )


@app.route("/classes/<int:class_id>/delete", methods=["POST"])
def delete_class(class_id):
    connection = get_connection()

    connection.execute(
        "DELETE FROM classes WHERE id = ?",
        (class_id,),
    )

    connection.commit()
    connection.close()

    return redirect("/classes")


@app.route("/classes/<int:class_id>/students", methods=["GET", "POST"])
def manage_enrollment(class_id):
    connection = get_connection()

    class_item = connection.execute(
        """
        SELECT id, subject_code, subject_name, section
        FROM classes
        WHERE id = ?
        """,
        (class_id,),
    ).fetchone()

    if class_item is None:
        connection.close()
        return "Class schedule not found", 404

    if request.method == "POST":
        student_id = request.form.get("student_id", type=int)

        if student_id is not None:
            connection.execute(
                """
                INSERT OR IGNORE INTO enrollments
                (class_id, student_id)
                VALUES (?, ?)
                """,
                (class_id, student_id),
            )
            connection.commit()

    enrolled_students = connection.execute(
        """
        SELECT students.id, students.student_number, students.full_name
        FROM students
        INNER JOIN enrollments
            ON students.id = enrollments.student_id
        WHERE enrollments.class_id = ?
        ORDER BY students.full_name
        """,
        (class_id,),
    ).fetchall()

    available_students = connection.execute(
        """
        SELECT id, student_number, full_name
        FROM students
        WHERE id NOT IN (
            SELECT student_id
            FROM enrollments
            WHERE class_id = ?
        )
        ORDER BY full_name
        """,
        (class_id,),
    ).fetchall()

    connection.close()

    return render_template(
        "enrollment.html",
        class_item=class_item,
        enrolled_students=enrolled_students,
        available_students=available_students,
    )


@app.route(
    "/classes/<int:class_id>/students/<int:student_id>/remove",
    methods=["POST"],
)
def remove_enrollment(class_id, student_id):
    connection = get_connection()

    connection.execute(
        """
        DELETE FROM enrollments
        WHERE class_id = ?
        AND student_id = ?
        """,
        (class_id, student_id),
    )

    connection.commit()
    connection.close()

    return redirect(f"/classes/{class_id}/students")


@app.route(
    "/classes/<int:class_id>/attendance",
    methods=["GET", "POST"],
)
def record_attendance(class_id):
    connection = get_connection()

    class_item = connection.execute(
        """
        SELECT id, subject_code, subject_name, section
        FROM classes
        WHERE id = ?
        """,
        (class_id,),
    ).fetchone()

    if class_item is None:
        connection.close()
        return "Class schedule not found", 404

    attendance_date = request.values.get(
        "attendance_date",
        date.today().isoformat(),
    )

    if request.method == "POST":
        student_ids = request.form.getlist("student_id", type=int)
        statuses = request.form.getlist("status")

        if len(student_ids) != len(statuses):
            connection.close()
            return "Attendance form data is invalid", 400

        for student_id, status in zip(student_ids, statuses):
            if status not in VALID_ATTENDANCE_STATUSES:
                connection.close()
                return "Invalid attendance status", 400

            connection.execute(
                """
                INSERT INTO attendance
                (
                    class_id,
                    student_id,
                    attendance_date,
                    status
                )
                VALUES (?, ?, ?, ?)
                ON CONFLICT(
                    class_id,
                    student_id,
                    attendance_date
                )
                DO UPDATE SET status = excluded.status
                """,
                (
                    class_id,
                    student_id,
                    attendance_date,
                    status,
                ),
            )

        connection.commit()

    enrolled_students = connection.execute(
        """
        SELECT students.id, students.student_number, students.full_name
        FROM students
        INNER JOIN enrollments
            ON students.id = enrollments.student_id
        WHERE enrollments.class_id = ?
        ORDER BY students.full_name
        """,
        (class_id,),
    ).fetchall()

    existing_records = connection.execute(
        """
        SELECT student_id, status
        FROM attendance
        WHERE class_id = ?
        AND attendance_date = ?
        """,
        (class_id, attendance_date),
    ).fetchall()

    existing_statuses = {
        record["student_id"]: record["status"]
        for record in existing_records
    }

    connection.close()

    return render_template(
        "attendance.html",
        class_item=class_item,
        enrolled_students=enrolled_students,
        attendance_date=attendance_date,
        existing_statuses=existing_statuses,
    )


if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)