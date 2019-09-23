import os
import subprocess
import hashlib
import time
import datetime
import shutil
import uuid
from pathlib import Path  
import codecs
import sys
import xml.dom.minidom

def absolute_file_paths(directory:str):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))

def get_sha256_of_file(file:str):
    sha256 = hashlib.sha256()
    with open(file, "rb") as fileObject:
        for chunk in iter(lambda: fileObject.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def file_is_empty(file:str):
    return os.stat(file).st_size == 0

def execute(program:str, arguments:str, workingdirectory:str="",timeout=120):
    if not os.path.isabs(workingdirectory):
        workingdirectory=os.path.abspath(workingdirectory)
    exit_code = subprocess.call(program + " " + arguments, cwd=workingdirectory, timeout=timeout)
    return exit_code

def ensure_directory_exists(path:str):
    if(not os.path.isdir(path)):
        os.makedirs(path)

def ensure_file_exists(path:str):
    if(not os.path.isfile(path)):
        with open(path,"a+") as f:
            pass

def ensure_file_does_not_exist(path:str):
    if(os.path.isfile(path)):
        os.remove(path)

def commit(directory:str, message:str):
    execute("git","add -A", directory, 3600)
    execute("git","commit -m \""+message+"\"",directory)

def get_time_from_internet():
    import ntplib
    response = ntplib.NTPClient().request('pool.ntp.org')
    return datetime.datetime.fromtimestamp(response.tx_time)

def format_xml_file(file:str, encoding:str):
    with codecs.open(file, 'r', encoding=encoding) as f:
        text = f.read()
    text=xml.dom.minidom.parseString(text).toprettyxml()
    with codecs.open(file, 'w', encoding=encoding) as f:
        f.write(text)


def get_clusters_and_sectors(dispath:str):
    import ctypes
    sectorsPerCluster = ctypes.c_ulonglong(0)
    bytesPerSector = ctypes.c_ulonglong(0)
    rootPathName = ctypes.c_wchar_p(dispath)
    ctypes.windll.kernel32.GetDiskFreeSpaceW(rootPathName, ctypes.pointer(sectorsPerCluster), ctypes.pointer(bytesPerSector), None, None)
    return (sectorsPerCluster.value, bytesPerSector.value)

def write_content_to_random_file(content:str):
    temp_file=str(uuid.uuid4())
    written_files.append(temp_file)
    with open(temp_file, 'w+') as f:
        f.write(file_content)
    return temp_file

def wipe_disk(diskpath:str, iterations=1):
    total, used, free = shutil.disk_usage(diskpath)
    id = str(uuid.uuid4())
    temp_folder=diskpath+os.linesep+id
    ensure_directory_exists(temp_folder)
    original_working_directory=os.getcwd()
    content_char="x"
    try:
        for iteration_number in list(range(iterations)):
            print("Start iteration "+str(iteration_number+1)+"...")
            os.chdir(temp_folder)
            total, used, free = shutil.disk_usage(diskpath)
            clusters_and_sectors=get_clusters_and_sectors(diskpath)
            written_files=[]
            file_size=clusters_and_sectors[0]*clusters_and_sectors[1]
            file_content=content_char * file_size
            while file_size < free:
                written_files.append(create_file(file_content))
                total, used, free = shutil.disk_usage(diskpath)
            if 0 < free:
                written_files.append(create_file(free))
            for file in written_files:
                os.remove(file)
    finally:
        os.chdir(original_working_directory)

def extract_archive_with_7z(unzip_file:str, file:str, password:str, output_directory:str):
    password_set=not password is None
    file_name=Path(file).name
    file_folder=os.path.dirname(file)
    argument="x"
    if password_set:
        argument=argument+" -p\""+password+"\""
    argument=argument+" -o"+output_directory
    argument=argument+" "+file_name
    return execute(unzip_file,argument,file_folder)

