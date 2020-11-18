from fixture.load_dll import DllHelper
from fixture.load_dll_archive import DllHelper_video_archive
from fixture.load_dll_longterm_archive import DllHelper_longterm_archive
from model.input_data import *
from fixture.work_with_db import *
import pytest
import time
from shutil import copytree
import shutil
import os


@pytest.fixture()#(scope="session", autouse=True)
def fix(request):
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
    return fix

@pytest.fixture
def fix_video(request):
    fixture = DllHelper_video_archive()
    fix = DllHelper()
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<ARCHITECT>,enable_audit<1>,audit_interval_minutes<1>").encode("utf-8"))
    shutil.rmtree(r'C:\ISS_MEDIA', ignore_errors=True)
    copytree(archive_to_copy, path_to_copy)
    os.system('taskkill /f /im video.exe')
    time.sleep(5)
    #copytree(archive_to_copy, path_to_copy)
    # функция disconnect передается в качестве параметра
    request.addfinalizer(fixture.disconnect)

    def fin():
        #shutil.rmtree("C:\\ISS_MEDIA")
        db = DbHelper(host="localhost", dbname="protocol", user="postgres", password="postgres")
        db.clean_db()
        db.close_connection()
        time.sleep(2)
        shutil.rmtree(r'C:\ISS_MEDIA\INDEX', ignore_errors=True)
        shutil.rmtree(r'C:\ISS_MEDIA\CAM_202', ignore_errors=True)
    request.addfinalizer(fin)
    return fixture

@pytest.fixture
def fix_longterm_archive(request):
    fixture = DllHelper_longterm_archive()
    fix = DllHelper()
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<ARCHITECT>,enable_audit<1>,audit_interval_minutes<1>").encode("utf-8"))
    copytree(archive_to_copy, path_to_copy_longterm)
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<ARCHIVER>,objid<" + archiver_id + ">,parent_id<" + slave + ">,name<" + archiver_name + ">").encode("utf-8"))
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<ARCHIVER>,objid<" + archiver_id + ">,parent_id<" + slave + ">,drives_and_folders" + archiver_drivers + "").encode("utf-8"))

    def fin():
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<ARCHIVER>,objid<" + archiver_id + ">").encode("utf-8"))
        shutil.rmtree("C:\\ARCHIVE\\ISS_MEDIA")
        db = DbHelper(host="localhost", dbname="protocol", user="postgres", password="postgres")
        db.clean_db()
        db.close_connection()
    request.addfinalizer(fin)
    return fixture
