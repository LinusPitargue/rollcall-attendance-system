import sqlite3

from flask import Flask, redirect, render_template, request

from database import get_connection, initialize_database


app = Flask(__name__)


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


if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)