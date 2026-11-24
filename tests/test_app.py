import sys
from pathlib import Path


PROJECT_FOLDER = Path(__file__).resolve().parents[1]

if str(PROJECT_FOLDER) not in sys.path:
    sys.path.insert(0, str(PROJECT_FOLDER))


import database
import pytest

from app import app
from database import initialize_database

if str(PROJECT_FOLDER) not in sys.path:
    sys.path.insert(0, str(PROJECT_FOLDER))


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