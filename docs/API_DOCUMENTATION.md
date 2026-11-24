# RollCall API Documentation

## 1. API Overview

RollCall uses an external public holiday API to check whether the selected attendance date is a Philippine public holiday.

If the selected date is a public holiday, the system prevents attendance from being saved.

## 2. API Provider

Provider: Nager.Date

Website:

https://nagerholidays.com

## 3. Endpoint

The application uses:

    https://nagerholidays.com/api/v4/Holidays/PH/{year}

Example:

    https://nagerholidays.com/api/v4/Holidays/PH/2026

The country code PH represents the Philippines.

## 4. HTTP Method

The application uses the GET method to retrieve public holiday information.

## 5. Request Parameters

| Parameter | Description                      | Example |
| --------- | -------------------------------- | ------- |
| PH        | Country code for the Philippines | PH      |
| year      | Year of the attendance date      | 2026    |

## 6. API Workflow

1. The teacher selects an attendance date.
2. RollCall extracts the year from the date.
3. The system sends a GET request to the API.
4. The API returns holiday data in JSON format.
5. RollCall compares the selected date with the returned holiday dates.
6. If a holiday is found, attendance saving is disabled.
7. If no holiday is found, attendance can be saved.

## 7. Example Request

    GET https://nagerholidays.com/api/v4/Holidays/PH/2026

## 8. Example Response

    [
        {
            "date": "2026-12-25",
            "name": "Christmas Day",
            "countryCode": "PH",
            "nationalHoliday": true,
            "holidayTypes": [
                "Public"
            ]
        }
    ]

## 9. Response Fields Used

| Field           | Description                                | Used by RollCall |
| --------------- | ------------------------------------------ | ---------------- |
| date            | Date of the holiday                        | Yes              |
| name            | Name of the holiday                        | Yes              |
| countryCode     | Country associated with the holiday        | No               |
| nationalHoliday | Indicates whether it is a national holiday | No               |
| holidayTypes    | Type of holiday                            | No               |

RollCall mainly uses the date and name fields.

## 10. Source Code Integration

The API communication is located in:

    holiday_service.py

The main function is:

    check_public_holiday(attendance_date)

This function sends the request, processes the JSON response, finds matching holidays, and handles request errors.

The attendance route in app.py calls this function before saving attendance.

## 11. Successful API Request

If no holiday matches the selected date, the teacher can save attendance.

If a holiday matches the selected date, the system displays a message such as:

    Attendance cannot be saved because Christmas Day is a public holiday.

## 12. Error Handling

The application handles:

- No internet connection
- API server unavailability
- Request timeout
- Invalid JSON responses
- Unexpected API errors

The system displays:

    The public holiday API could not be reached. Please verify the date manually.

The application does not terminate unexpectedly when the API fails.

## 13. Authentication

The current API integration does not require an API key or password.

No API credentials are stored in the repository.

## 14. Security Considerations

The application:

- Uses a request timeout.
- Uses a fixed API provider URL.
- Does not accept arbitrary URLs from users.
- Does not store API credentials.
- Does not send private student information to the API.

Only the selected attendance year is included in the request.

## 15. API Limitations

The API provides public holiday information but does not provide the school’s complete academic calendar.

Teachers must still verify school suspensions, special school holidays, examinations, and campus-specific non-class days.

## 16. Testing

The API integration is tested using mocked responses instead of relying on a live internet connection.

The tests verify that:

- A holiday can be identified.
- Network errors are handled.
- Attendance is blocked on a holiday.
- Attendance can be saved when no holiday is found.

The tests are located in:

    tests/test_app.py

## 17. Reference

Nager.Date. (n.d.). Nager.Date public holiday API.

https://nagerholidays.com
