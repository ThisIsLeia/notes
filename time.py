from delorean import Delorean
from dateutil.relativedelta import relativedelta
import pytz
from datetime import datetime, timedelta

# constants
LOCAL_TZ = 'Asia/Shanghai'

def start_of_day_as_utc(local_tz=None):
    return Delorean(local_tz, timezone=LOCAL_TZ).start_of_day.astimezone(pytz.UTC)

def test():
    date_time = Delorean(timezone=LOCAL_TZ).datetime
    print(date_time)

    # date_time = Delorean().start_of_day.astimezone(pytz.UTC)
    # print(date_time)
    #
    # date_time_2 = datetime.utcnow()
    # print(date_time_2)
    #
    # # start_of_day -> 時間會變成 00:00:00
    # today_start = Delorean(datetime=date_time).start_of_day
    # print(today_start)
    #
    # 區間 (months 注意有s!!!)
    start = Delorean(datetime=date_time.replace(day=1)).start_of_day+relativedelta(months=1)
    start = (Delorean(timezone=LOCAL_TZ).datetime - relativedelta(months=1)).astimezone(pytz.UTC)
    print(start)
    #

    # end = (start + relativedelta(months=1)).astimezone(pytz.UTC)
    # print(end)
    #
    # now = Delorean(timezone=LOCAL_TZ).datetime
    # print('now', now)

    # now = datetime.now()
    # this_week_start = now - timedelta(days=now.weekday())
    # this_week_end = now + timedelta(days=6 - now.weekday())
    # print('--- this_week_start = {} this_week_end = {}'.format(this_week_start, this_week_end))
    # print(timedelta(days=now.weekday()))

    # now = Delorean(timezone=LOCAL_TZ).start_of_day
    # print("now==>", now)
    # this_week_start = now - timedelta(days=now.weekday())
    # print("this_week_start==>", this_week_start)
    # this_week_end = now + timedelta(days=6 - now.weekday())
    # print("this_week_end==>", this_week_end)

    # now = Delorean(timezone=LOCAL_TZ).start_of_day
    # print("now==>", now)
    # week_start = now - timedelta(days=now.weekday())
    # # week_end = now + timedelta(days=6 - now.weekday())
    # print("this_week_start==>", week_start)
    # week_end = week_start + timedelta(days=7) - timedelta(microseconds=1)
    # print("this_week_end==>", week_end)


if __name__ == '__main__':
    test()
