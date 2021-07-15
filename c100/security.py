import cv2
import dropbox
import time
import random 
StartTime=time.time()
def takeSnapShot():
    num=random.randint(0,100)
    voc=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=voc.read()
        imageName="img"+str(num)+".png"
        cv2.imwrite(imageName,frame)
        StartTime=time.time()
        result=False
    return imageName
    print("snapshot taken")
    voc.release()
    cv2.destroyAllWindows()

def uploadFile(soure):
    accesstoken='sl.A0lcuVPvjRAFpMmCQQUG9X1C8Ka_zTcCevuBdJVb_ngk0-O41PAac62330FxzQwrzUsk45PAFjQMfLY7Tnu3yl1cUQz08E-TJnYh9OQczCISPJfH6UlzyJ4lTIgqorzTZvjyvrgshx-V'
    source=soure
    dest="/security/"+soure
    dbx=dropbox.Dropbox(accesstoken)
    s=open(soure,'rb')
    dbx.files_upload(s.read(),dest,mode=dropbox.files.WriteMode.overwrite)
    print("files uploaded")

def main():
    while(True):
        if((time.time()-StartTime)>=300):
            name=takeSnapShot()
            uploadFile(name)

main()