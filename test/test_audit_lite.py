from fixture.work_with_db import DbHelper
import time
from model.input_data import *
from fixture.take_datetime import *


def test_setup(fix):
    starttime, starttime2, starttime3, starttime4 = take_datetimes()
    fix.send_react(("MEDIA_CLIENT|1|ADD_SEQUENCE|mode<1x1>,seq<|"+camId+">").encode("UTF-8"))
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<ARCHITECT>,enable_audit<1>").encode("utf-8"))
    time.sleep(2)
    db = DbHelper(host="localhost", dbname="protocol", user="postgres", password="postgres")
    assert db.records != []
    time.sleep(1)
    db.check_db_events(event_time=starttime)
    time.sleep(2)
    t = take_datetime_from_db_timeto(db)
    #проверка текущего времени и времени записанного в БД
    assert t == starttime or t == starttime2 or t == starttime3 or t == starttime4
    event_id = db.records[0][0]
    #print(event_id)
    db.check_db_objects(event_id=event_id)
    assert db.records[0][3] == camId
    db.check_db_intervals(event_id=event_id)
    t2 = take_datetime_from_db_timefrom(db)
    t3 = take_datetime_from_db_timeto(db)
    assert t2 <= t <= t3


def test2(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<ARCHITECT>,enable_audit<1>,audit_interval_minutes<1>").encode("utf-8"))
    t1 = take_datetime()
    time.sleep(61)
    t2 = take_datetime()
    db = DbHelper(host="localhost", dbname="protocol", user="postgres", password="postgres")
    db.check_db_events(event_time=t1)
    time.sleep(5)
    #print(db.records)
    t3 = take_datetime_from_db_timeto(db)
    assert t1 <= t3 <= t2


