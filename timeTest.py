from datetime import datetime, timedelta
import pytz


def gps_datetime(time_week, time_ms, leap_seconds):
    gps_epoch = datetime(1980, 1, 6, tzinfo=pytz.utc)
    # gps_time - utc_time = leap_seconds
    return gps_epoch + timedelta(weeks=time_week, milliseconds=time_ms, seconds=-leap_seconds)


# YUN_0001.JPG,95895.143000,2134
# t = gps_datetime(2077, 295584830.0,18.0)
t = gps_datetime(2134, 95895, 143000)
print(t)
