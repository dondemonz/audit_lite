from ctypes import windll, WINFUNCTYPE, c_int, c_char_p, c_ulong, c_uint32
from model.input_data import *

p1 = c_char_p(localHostIp.encode("utf-8"))
p2 = c_char_p(iidkPort.encode("utf-8"))
p3 = c_char_p(iidkId.encode("utf-8"))
# message = c_char_p("CORE", "RANDOM", "CREATE_OBJECT", "objtype", "CAM", "objid", "999999", "parent_id", "2", "name", "Test Camera")
p5 = 0
p6 = 0
p7 = 0


class DllHelper:
    def __init__(self, message=None, cb1=None, cb2=None, cb3=None, obj_name=None, obj_id=None):
        self.my_dll = windll.LoadLibrary("iidk.dll")
        self.ConnectEx = self.my_dll.ConnectEx
        self.Disconnect = self.my_dll.Disconnect
        self.SendDoReact = self.my_dll.SendDoReact
        self.message = message
        self.objName = obj_name
        self.objId = obj_id
        self.cb1 = cb1
        self.cb2 = cb2
        self.cb3 = cb3


    def callback(self, cb1, cb2, cb3):
        # сохранение параметра в общей переменной
        # print(cb1, cb2, cb3)
        self.cb1 = cb1
        return 0

    def callback_proto(self):
        global CallbackProto
        CallbackProto = WINFUNCTYPE(c_int, c_char_p, c_char_p, c_ulong)

    def callback_wrapper(self):
        global CallbackWrapper
        CallbackWrapper = CallbackProto(self.callback)

    def connect(self):
        self.my_dll.ConnectEx.argtypes = [c_char_p, c_char_p, c_char_p, CallbackProto, c_uint32, c_int, c_uint32]
        self.my_dll.ConnectEx(p1, p2, p3, CallbackWrapper, p5, p6, p7)
        """проверка isconected
        if x == 0:
            print("error")
        else:
            print("ok")
        """

    def send_react(self, message):
        self.connect_to_dll()
        # message = ("CORE", "RANDOM", "CREATE_OBJECT", "objtype", "CAM", "objid", "999999", "parent_id", "2", "name", "Test Camera")
        msg = c_char_p(message)
        self.my_dll.SendDoReact.argtypes = [c_char_p, c_char_p]
        self.my_dll.SendDoReact(p3, msg)

    def send_event(self, message):
        self.connect_to_dll()
        # message = "CORE||CREATE_OBJECT|objtype<CAM>,objid<99>,parent_id<2>,name<Test_Camera>".encode("utf-8")
        msg = c_char_p(message)
        self.my_dll.SendMsg.argtypes = [c_char_p, c_char_p]
        self.my_dll.SendMsg(p3, msg)

    def disconnect(self):
        self.my_dll.Disconnect(iidkId)


    def connect_to_dll(self):
        self.callback_proto()
        self.callback_wrapper()
        self.connect()

"""
    def is_object_exist(self, obj_name, obj_id):
        self.my_dll.
"""



# print(my_dll)
# print(vars(my_dll))

# message = (p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20)
# message = "CORE||CREATE_OBJECT|objtype<CAM>,objid<99>,parent_id<2>,name<Test_Camera>".encode("utf-8")
# message = "CAM|40|REC".encode("utf-8")