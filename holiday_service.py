import requests


HOLIDAY_API_URL = (
    "https://nagerholidays.com/api/v4/Holidays/PH/{year}"
)


def check_public_holiday(attendance_date):
    """
    Check whether a date is a Philippine public holiday.

    Returns:
        holiday information and None if successful.
        None and an error message if the API request fails.
    """
    year = attendance_date[:4]
    url = HOLIDAY_API_URL.format(year=year)

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        holidays = response.json()

        for holiday in holidays:
            if holiday.get("date") == attendance_date:
                return holiday, None

        return None, None

    except requests.RequestException as error:
        return None, str(error)

    except ValueError as error:
        return None, str(error)