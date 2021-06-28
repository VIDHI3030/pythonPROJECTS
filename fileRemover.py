import time
import calendar
import os
import shutil

path = input("Enter path: ")
days = input("Enter days before which you want to delete files': ")
seconds = time.time() - (days * 24 * 60 * 60)
if os.path.exists(path):
    listoffiles = os.listdir(path)
    for f in listoffiles:
        name, ext = os.path.splitext(f)
        newPath = path + "/" + name
        ftime = os.stat(newPath).st_ctime)
        fileTime = time.time() - ftime
        if(fileTime<seconds):
            os.remove(newPath)
else:
    print("Path not found")