import sys
from pathlib import Path


PROJECT_FOLDER = Path(__file__).resolve().parents[1]

if str(PROJECT_FOLDER) not in sys.path:
    sys.path.insert(0, str(PROJECT_FOLDER))


import app as app_module
import database
import holiday_service
import pytest
import requests

from app import app
from database import initialize_database


@pytest.fixture()
def client(tmp_path, monkeypatch):
    test_database = tmp_path / "test_rollcall.db"

    monkeypatch.setattr(
        database,
        "DATABASE_PATH",
        test_database,
    )

    initialize_database()

    app.config.update(
        TESTING=True,
    )

    with app.test_client() as test_client:
        yield test_client


def add_test_student(client):
    client.post(
        "/students/new",
        data={
            "student_number": "2026-001",
            "full_name": "Juan Dela Cruz",
            "email": "juan@example.com",
        },
    )


def get_student_id():
    connection = database.get_connection()

    student = connection.execute(
        """
        SELECT id
        FROM students
        WHERE student_number = ?
        """,
        ("2026-001",),
    ).fetchone()

    connection.close()

    return student["id"]


def add_test_class(client):
    client.post(
        "/classes/new",
        data={
            "subject_code": "CS101",
            "subject_name": "Programming 1",
            "section": "BSCS 2A",
            "room": "Laboratory 2",
            "meeting_day": "Monday",
            "start_time": "08:00",
            "end_time": "10:00",
        },
    )


def get_class_id():
    connection = database.get_connection()

    class_item = connection.execute(
        """
        SELECT id
        FROM classes
        WHERE subject_code = ?
        """,
        ("CS101",),
    ).fetchone()

    connection.close()

    return class_item["id"]


def test_home_page_loads(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"RollCall" in response.data


def test_student_can_be_added(client):
    response = client.post(
        "/students/new",
        data={
            "student_number": "2026-001",
            "full_name": "Juan Dela Cruz",
            "email": "juan@example.com",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Juan Dela Cruz" in response.data
    assert b"2026-001" in response.data


def test_student_requires_number_and_name(client):
    response = client.post(
        "/students/new",
        data={
            "student_number": "",
            "full_name": "",
            "email": "",
        },
    )

    assert response.status_code == 200
    assert b"Student number and full name are required." in response.data


def test_duplicate_student_number_is_rejected(client):
    add_test_student(client)

    response = client.post(
        "/students/new",
        data={
            "student_number": "2026-001",
            "full_name": "Another Student",
            "email": "another@example.com",
        },
    )

    assert response.status_code == 200
    assert b"That student number already exists." in response.data


def test_student_can_be_edited(client):
    add_test_student(client)

    student_id = get_student_id()

    response = client.post(
        f"/students/{student_id}/edit",
        data={
            "student_number": "2026-001",
            "full_name": "Juan Updated",
            "email": "updated@example.com",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Juan Updated" in response.data
    assert b"updated@example.com" in response.data


def test_student_can_be_deleted(client):
    add_test_student(client)

    student_id = get_student_id()

    response = client.post(
        f"/students/{student_id}/delete",
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Juan Dela Cruz" not in response.data


def test_class_schedule_can_be_added(client):
    response = client.post(
        "/classes/new",
        data={
            "subject_code": "CS101",
            "subject_name": "Programming 1",
            "section": "BSCS 2A",
            "room": "Laboratory 2",
            "meeting_day": "Monday",
            "start_time": "08:00",
            "end_time": "10:00",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"CS101" in response.data
    assert b"Programming 1" in response.data


def test_class_rejects_invalid_time(client):
    response = client.post(
        "/classes/new",
        data={
            "subject_code": "CS102",
            "subject_name": "Programming 2",
            "section": "BSCS 2A",
            "room": "Laboratory 3",
            "meeting_day": "Tuesday",
            "start_time": "10:00",
            "end_time": "08:00",
        },
    )

    assert response.status_code == 200
    assert b"End time must be later than start time." in response.data


def test_holiday_api_finds_holiday(monkeypatch):
    class FakeResponse:
        def raise_for_status(self):
            return None

        def json(self):
            return [
                {
                    "date": "2026-12-25",
                    "name": "Christmas Day",
                }
            ]

    def fake_get(url, timeout):
        return FakeResponse()

    monkeypatch.setattr(
        holiday_service.requests,
        "get",
        fake_get,
    )

    holiday, error = holiday_service.check_public_holiday(
        "2026-12-25"
    )

    assert error is None
    assert holiday["name"] == "Christmas Day"


def test_holiday_api_handles_network_error(monkeypatch):
    def fake_get(url, timeout):
        raise requests.RequestException("API unavailable")

    monkeypatch.setattr(
        holiday_service.requests,
        "get",
        fake_get,
    )

    holiday, error = holiday_service.check_public_holiday(
        "2026-12-25"
    )

    assert holiday is None
    assert error is not None


def test_attendance_can_be_recorded_and_reported(
    client,
    monkeypatch,
):
    monkeypatch.setattr(
        app_module,
        "check_public_holiday",
        lambda attendance_date: (None, None),
    )

    add_test_student(client)
    add_test_class(client)

    student_id = get_student_id()
    class_id = get_class_id()

    client.post(
        f"/classes/{class_id}/students",
        data={
            "student_id": student_id,
        },
    )

    attendance_response = client.post(
        f"/classes/{class_id}/attendance",
        data={
            "attendance_date": "2026-11-24",
            "student_id": str(student_id),
            "status": "Present",
        },
        follow_redirects=True,
    )

    assert attendance_response.status_code == 200
    assert b"Attendance saved successfully." in attendance_response.data

    report_response = client.get("/reports")

    assert report_response.status_code == 200
    assert b"Juan Dela Cruz" in report_response.data
    assert b"100.00%" in report_response.data


def test_attendance_is_blocked_on_holiday(
    client,
    monkeypatch,
):
    monkeypatch.setattr(
        app_module,
        "check_public_holiday",
        lambda attendance_date: (
            {
                "name": "Christmas Day",
            },
            None,
        ),
    )

    add_test_student(client)
    add_test_class(client)

    student_id = get_student_id()
    class_id = get_class_id()

    client.post(
        f"/classes/{class_id}/students",
        data={
            "student_id": student_id,
        },
    )

    response = client.post(
        f"/classes/{class_id}/attendance",
        data={
            "attendance_date": "2026-12-25",
            "student_id": str(student_id),
            "status": "Present",
        },
    )

    assert response.status_code == 200
    assert b"Attendance was not saved" in response.data

    connection = database.get_connection()

    record_count = connection.execute(
        "SELECT COUNT(*) AS count FROM attendance"
    ).fetchone()["count"]

    connection.close()

    assert record_count == 0