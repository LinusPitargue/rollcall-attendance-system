from flask import Flask

from database import initialize_database


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


if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)