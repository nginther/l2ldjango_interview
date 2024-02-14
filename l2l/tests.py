from django.test import TestCase
from datetime import datetime
from l2l.templatetags import l2l_extras


class DatetimeConversionTests(TestCase):
    # Input constants used for tests. All values are different formats with equivalent values
    DT_ISO_STRING = "2024-02-12T12:34:56"
    DT_ISO_STRING_WITH_TIMEZONE = "2024-02-12T12:34:56Z"
    DT_OBJECT = datetime(2024, 2, 12, 12, 34, 56)
    EXPECTED_DT = "2024-02-12 12:34:56"

    def test_converted_iso_string(self):
        """
       l2l_dt takes a datetime string in the format of "%Y-%m-%dT%H:%M:%S"
       and returns a datetime string in the format of "%Y-%m-%d %H:%M:%S"
        """
        response = l2l_extras.l2l_dt(self.DT_ISO_STRING)
        self.assertEqual(response, self.EXPECTED_DT)

    def test_converted_datetime_object(self):
        """
       l2l_dt takes a datetime object and returns a datetime string
       in the format of "%Y-%m-%d %H:%M:%S"
        """
        response = l2l_extras.l2l_dt(self.DT_OBJECT)
        self.assertEqual(response, self.EXPECTED_DT)

    def test_invalid_date_error_string_contents(self):
        """
      Validate the l2l_dt invalid date error message has the expected value
        """
        expected_error_message = "Invalid date provided"
        self.assertEqual(l2l_extras.INVALID_DATE_ERROR, expected_error_message)

    def test_invalid_date_string_returns_error(self):
        """
       l2l_dt returns a error message if the string is not a valid datetime
        """
        response = l2l_extras.l2l_dt("02-02-2024")
        self.assertEqual(response, l2l_extras.INVALID_DATE_ERROR)

    def test_timezone_unsupported_error_message(self):
        """
       Validate the l2l_dt timezone error message has the expected value
        """
        expected_error_message = "Timezones are not supported"
        self.assertEqual(l2l_extras.TIMEZONE_UNSUPPORTED_ERROR, expected_error_message)

    def test_iso_string_with_timezone_produces_error(self):
        """
       l2l_dt returns an error message if the input datetime has a timezone provided
        """
        response = l2l_extras.l2l_dt(self.DT_ISO_STRING_WITH_TIMEZONE)
        self.assertEqual(response, l2l_extras.TIMEZONE_UNSUPPORTED_ERROR)
