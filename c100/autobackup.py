import cv2
import time
import random

import os
import dropbox
from dropbox.files import WriteMode
#
class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token
#
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

            # enumerate local files recursively
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                    # construct the full local path
                local_path = os.path.join(root, filename)

                    # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                    # upload the file
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    while(True):
        if((time.time()-startTime) >= 3600):
            accesstoken='sl.A0lcuVPvjRAFpMmCQQUG9X1C8Ka_zTcCevuBdJVb_ngk0-O41PAac62330FxzQwrzUsk45PAFjQMfLY7Tnu3yl1cUQz08E-TJnYh9OQczCISPJfH6UlzyJ4lTIgqorzTZvjyvrgshx-V'
            cd=TransferData(accesstoken)
            soure=input("enter the file path to trasfer: ")
            dest=input("enter the upload location: ")
            cd.uploadFile(soure,dest)
            print("files have been moved")

main()
