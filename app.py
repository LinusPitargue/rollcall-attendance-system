import sqlite3

from flask import Flask,redirect, render_template, request

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

    return render_template("student_form.html", error=error)

if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)