from fixture.work_with_db import DbHelper
import time
from model.input_data import *
from fixture.take_datetime import *


def test_check_audit_works(fix):
    starttime, starttime2, starttime3, starttime4 = take_datetimes()
    fix.send_react(("MEDIA_CLIENT|1|ADD_SEQUENCE|mode<1x1>,seq<|" + cam_id + ">").encode("UTF-8"))
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<ARCHITECT>,enable_audit<1>").encode("utf-8"))
    time.sleep(2)
    db = DbHelper(dbname=db_protocol)
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
    assert db.records[0][3] == cam_id
    db.check_db_intervals(event_id=event_id)
    t2 = take_datetime_from_db_timefrom(db)
    t3 = take_datetime_from_db_timeto(db)
    assert t2 <= t <= t3


def test_check_audit_interval_1_minute(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<ARCHITECT>,enable_audit<1>,audit_interval_minutes<1>").encode("utf-8"))
    t1 = take_datetime()
    time.sleep(61)
    t2 = take_datetime()
    db = DbHelper(dbname=db_protocol)
    db.check_db_events(event_time=t1)
    time.sleep(5)
    #print(db.records)
    t3 = take_datetime_from_db_timeto(db)
    assert t1 <= t3 <= t2

def test_check_audit_intervals_in_db(fix):
    db = DbHelper(dbname=db_securos)
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<ARCHITECT>,enable_audit<1>,audit_interval_minutes<10>").encode("utf-8"))
    db.check_db_audit_interval(system_name="cистема")
    assert db.records[0][11] == 10
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<ARCHITECT>,enable_audit<1>,audit_interval_minutes<15>").encode("utf-8"))
    db.check_db_audit_interval(system_name="Система")
    assert db.records[0][11] == 15
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<ARCHITECT>,enable_audit<1>,audit_interval_minutes<30>").encode("utf-8"))
    db.check_db_audit_interval(system_name="Система")
    assert db.records[0][11] == 30
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<ARCHITECT>,enable_audit<1>,audit_interval_minutes<60>").encode("utf-8"))
    db.check_db_audit_interval(system_name="Система")
    assert db.records[0][11] == 60


def test_check_audit_interval_5_minute(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<ARCHITECT>,enable_audit<1>,audit_interval_minutes<5>").encode("utf-8"))
    t1 = take_datetime()
    time.sleep(303)
    t2 = take_datetime()
    db = DbHelper(dbname=db_protocol)
    db.check_db_events(event_time=t1)
    time.sleep(5)
    print(db.records)
    t3 = take_datetime_from_db_timeto(db)
    assert t1 <= t3 <= t2