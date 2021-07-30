import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
       
    def upload_file(self,file_from, file_to):
        """upload a file to DropBox using Api v2 
        """
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for fileName in files:
                  local_path = os.path.join(root, fileName)
                  relative_path = os.path.relpath(local_path, file_from)
                  dropbox_path = os.path.join(file_to, relative_path)

                  with open(file_from,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token = 'A-6BvMN99AgAAAAAAAAAAbfsPJhXX1vpsW9sNmXZErTpxIqfvtTpGo9LyKZgDnQj'
    transferData = TransferData(access_token)

    file_from = input("Enter the file to upload")
    file_to = input("Enter the dropbox path")

    transferData.upload_file(file_from,file_to)

if __name__ == "__main__":
    main()