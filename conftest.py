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
def fix3(request):
    fix = DllHelper()
    #две камеры для тестов
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<GRABBER>,objid<" + camId + ">,parent_id<" + slave + ">,name<"+camName+">,type<Axis>,model<default>,format<H264>,ip<172.16.20.54>,user_name<root>,auth_crpt<LLGLBGFCECOAFKHN>").encode("utf-8"))  # type=Axis, т.к. без типа будет сильно грузиться система
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM>,objid<" + camId + ">,parent_id<" + camId + ">,name<"+camName+">").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<GRABBER>,objid<" + camId2 + ">,parent_id<" + slave + ">,name<"+camName2+">,type<Axis>,model<default>,format<H264>,ip<172.16.20.54>,user_name<root>,auth_crpt<LLGLBGFCECOAFKHN>").encode("utf-8"))  # type=Axis, т.к. без типа будет сильно грузиться система
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM>,objid<" + camId2 + ">,parent_id<" + camId2 + ">,name<"+camName2+">").encode("utf-8"))
    time.sleep(5)

    #print('\nSome recource')
    def fin():
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<GRABBER>,objid<" + camId + ">").encode("utf-8"))
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<GRABBER>,objid<" + camId2 + ">").encode("utf-8"))
        fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<ARCHITECT>,enable_audit<0>").encode("utf-8"))
        fix.disconnect()
        db = DbHelper(host="localhost", dbname="protocol", user="postgres", password="postgres")
        db.clean_db()
        db.close_connection()
        #print('\nSome resource fin')
    request.addfinalizer(fin)
    return request
