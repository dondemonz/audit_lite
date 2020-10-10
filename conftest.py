from fixture.load_dll import DllHelper
from model.input_data import *
from fixture.work_with_db import *
import pytest
import time


@pytest.fixture
def fix(request):
    fixture = DllHelper()
    # функция disconnect передается в качестве параметра
    request.addfinalizer(fixture.disconnect)
    return fixture

@pytest.fixture(scope="session", autouse=True)
def fix2(request):
    fix = DllHelper()
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<GRABBER>,objid<" + cam_id + ">,parent_id<" + slave + ">,name<" + cam_name + ">,type<Virtual>,model<default>,chan<14>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM>,objid<" + cam_id + ">,parent_id<" + cam_id + ">,name<" + cam_name + ">,,mux<13>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<GRABBER>,objid<" + cam_id2 + ">,parent_id<" + slave + ">,name<" + cam_name2 + ">,type<Virtual>,model<default>,chan<14>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM>,objid<" + cam_id2 + ">,parent_id<" + cam_id2 + ">,name<" + cam_name2 + ">,,mux<13>").encode("utf-8"))

    #print('\nSome recource')
    def fin():
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<GRABBER>,objid<" + cam_id + ">").encode("utf-8"))
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<GRABBER>,objid<" + cam_id2 + ">").encode("utf-8"))
        fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<ARCHITECT>,enable_audit<0>").encode("utf-8"))
        fix.disconnect()
        db = DbHelper(host="localhost", dbname="protocol", user="postgres", password="postgres")
        db.clean_db()
        db.close_connection()
        #print('\nSome resource fin')
    request.addfinalizer(fin)
    return request
