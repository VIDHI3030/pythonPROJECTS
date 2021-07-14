import dropbox 
class TransferData:
    def __init__(self,accesstoken):
        self.accesstoken=accesstoken
    def uploadFile(self,soure,dest):
        dbx=dropbox.Dropbox(self.accesstoken)
        s=open(soure,'rb')
        dbx.files_upload(s.read(),dest)
    

def main():
    accesstoken='sl.A0lcuVPvjRAFpMmCQQUG9X1C8Ka_zTcCevuBdJVb_ngk0-O41PAac62330FxzQwrzUsk45PAFjQMfLY7Tnu3yl1cUQz08E-TJnYh9OQczCISPJfH6UlzyJ4lTIgqorzTZvjyvrgshx-V'
    cd=TransferData(accesstoken)
    soure=input("enter the file path to trasfer: ")
    dest=input("enter the upload location: ")
    cd.uploadFile(soure,dest)
    print("files have been moved")

main()