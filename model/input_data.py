iidk_id = "1"
iidk_port_core = "1030"  # "1030"
iidk_port_video = "900"
iidk_port_archiver = "901"
local_host_ip = "172.16.11.102"  # "172.16.20.101"
user = "1"
password = "1"
auth = (user, password)  # пользователь/пароль
slave_ip = "172.16.11.102"
rest_port = "8887"
cam_id = "202"
cam_name = "cam 202"
cam_id2 = "45"
cam_name2 = "cam 45"
slave = "VQA-2"
headers = {"Content-Type": "application/json"}
person_name = "user2"
obj_id = "999"
person_id = "1.999"
department_id = "1.999"
export_path = "C:\\export\\"
id_db = "16394"  # id тестовой базы данных, названи таблицы image. В ней должно быть две колонки: 1-я image, 2-я id
event_action = "24"
keyword = 'SecurOS'
path = "C:\\Program Files (x86)\\ISS\\SecurOS\\"
db_protocol = "protocol"
db_securos = "securos"
sys = 'система'
archive_to_copy = "C:\\archive_for_audit_test\\ISS_MEDIA"
path_to_copy = "C:\\ISS_MEDIA"
path_to_copy_longterm = "C:\\ARCHIVE\\ISS_MEDIA\\"
op_archive = "оперативный архив"
long_archive = "долговременный архив"
archiver_id = "1"
archiver_name = "archiver"
archiver_drivers1 = '<{"drives": [{ "min_free_space" : 0.1 , "path" : "C:\\\\" , "permissions" : {"audio":"unused","video":"rw"}}], " iscsi_drives " : [] , "network_folders" : []}>'
archiver_drivers = str(archiver_drivers1)

tour_id = "0"  # Id настроенного тура
preset_id = "1"  # Id настроенной препозиции

"""
drives<>,drives_and_folders<{"drives":[{"min_free_space":0.1,"path":"C:\\","permissions":{"audio":"unused","video":"rw"}}],"iscsi_drives":[],"network_folders":[]}>,

у меня в тестах 
drives_and_folders<{'drives': [{'min_free_space': 0.1, 'path': 'C:\\', 'permissions': {'audio': 'unused', 'video': 'rw'}}], 'iscsi_drives': [], 'network_folders': []}>,
"""

