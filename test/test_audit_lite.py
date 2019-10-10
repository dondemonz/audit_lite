from fixture.work_with_db import DbHelper
from datetime import timedelta
import time
import datetime as dt
from model.input_data import *


keyword = 'SecurOS'
path = "C:\\Program Files (x86)\\ISS\\SecurOS\\"


def test_setup(fix):
    m = dt.datetime.now() + timedelta(hours=1)
    starttime = m.strftime("%Y-%m-%d %H:%M:%S")
    m2 = dt.datetime.now() + timedelta(hours=1, seconds=1)
    starttime2 = m2.strftime("%Y-%m-%d %H:%M:%S")
    fix.send_react(("MEDIA_CLIENT|1|ADD_SEQUENCE|mode<1x1>,seq<|"+camId+">").encode("UTF-8"))
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<ARCHITECT>,enable_audit<1>").encode("utf-8"))
    time.sleep(2)
    db = DbHelper(host="localhost", dbname="protocol", user="postgres", password="postgres")
    assert db.records != []
    db.check_db_events(event_time=starttime)
    time.sleep(1)
    datetime = db.records[0][3]
    t = datetime.strftime("%Y-%m-%d %H:%M:%S")
    #проверка текущего времени и времени записанного в БД
    assert t == starttime or t == starttime2
    event_id = db.records[0][0]
    print(event_id)
    db.check_db_objects(event_id=event_id)
    assert db.records[0][3] == camId
    db.check_db_intervals(event_id=event_id)
    time_from = db.records[0][2]
    t2 = time_from.strftime("%Y-%m-%d %H:%M:%S")
    time_to = db.records[0][3]
    t3 = time_to.strftime("%Y-%m-%d %H:%M:%S")
    assert t2 <= t <= t3

def test2(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<ARCHITECT>,enable_audit<1>,audit_interval_minutes<1>").encode("utf-8"))
    m = dt.datetime.now() + timedelta(hours=1)
    time.sleep(2)
    t1 = m.strftime("%Y-%m-%d %H:%M:%S")
    time.sleep(58)
    m2 = dt.datetime.now() + timedelta(hours=1)
    t2 = m2.strftime("%Y-%m-%d %H:%M:%S")
    db = DbHelper(host="localhost", dbname="protocol", user="postgres", password="postgres")
    db.check_db_events(event_time=t1)
    time.sleep(5)
    print(db.records)
    time_to = db.records[0][3]
    t3 = time_to.strftime("%Y-%m-%d %H:%M:%S")
    assert t1 <= t3 <= t2


def test_clean_db(fix):
    db = DbHelper(host="localhost", dbname="protocol", user="postgres", password="postgres")
    db.clean_db()
    db.close_connection()
