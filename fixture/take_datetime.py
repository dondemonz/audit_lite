import datetime as dt
from datetime import timedelta

def take_datetimes():
    m = dt.datetime.now() + timedelta(hours=1, seconds=1)
    starttime = m.strftime("%Y-%m-%d %H:%M:%S")
    m2 = dt.datetime.now() + timedelta(hours=1, seconds=2)
    starttime2 = m2.strftime("%Y-%m-%d %H:%M:%S")
    m3 = dt.datetime.now() + timedelta(hours=1, seconds=3)
    starttime3 = m3.strftime("%Y-%m-%d %H:%M:%S")
    m4 = dt.datetime.now() + timedelta(hours=1, seconds=4)
    starttime4 = m4.strftime("%Y-%m-%d %H:%M:%S")
    m5 = dt.datetime.now() + timedelta(hours=1, seconds=5)
    starttime5 = m5.strftime("%Y-%m-%d %H:%M:%S")
    return starttime, starttime2, starttime3, starttime4, starttime5

def take_datetime_from_db_timeto(db):
    time_to = db.records[0][3]
    t3 = time_to.strftime("%Y-%m-%d %H:%M:%S")
    return t3

def take_datetime_from_db_timefrom(db):
    time_from = db.records[0][2]
    t2 = time_from.strftime("%Y-%m-%d %H:%M:%S")
    return t2

def take_datetime_from_db_timefrom_second_row(db):
    time_from = db.records[1][2]
    t2 = time_from.strftime("%Y-%m-%d %H:%M:%S")
    return t2

def take_datetime():
    m = dt.datetime.now() + timedelta(hours=1)
    t1 = m.strftime("%Y-%m-%d %H:%M:%S")
    return t1