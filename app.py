from flask import Flask, render_template

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

if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)