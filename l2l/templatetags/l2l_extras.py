from django import template
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.template.defaultfilters import stringfilter

register = template.Library()

INVALID_DATE_ERROR = "Invalid date provided"
TIMEZONE_UNSUPPORTED_ERROR = "Timezones are not supported"
OUTPUT_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


@register.filter
@stringfilter
def l2l_dt(input_dt):
    """
    l2l_dt accepts either a datetime object or an ISO datetime without
    timezone information and returns a datetime of the format "%Y-%m-%d %H:%M:%S".
    An invalid datetime or a datetime with timezone information will return an error.
    """
    try:
        if timezone.is_aware(parse_datetime(input_dt)):
            return TIMEZONE_UNSUPPORTED_ERROR

        return (timezone.localtime(timezone.make_aware(parse_datetime(input_dt)))
                .strftime(OUTPUT_DATETIME_FORMAT))
    except ValueError:
        return INVALID_DATE_ERROR
    except AttributeError:
        return INVALID_DATE_ERROR
