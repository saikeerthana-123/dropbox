import dropbox
import os


class TransferData:
    def __init__(self, access_token):
        self.aT = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        fileName = os.path.split(file_from)[1]

        dropbox_file = '/CloudStorage/'+fileName

        with open(file_from, "rb") as f:
            dbx.files_upload(f.read(), dropbox_file,
                            mode=dropbox.files.WriteMode.overwrite)


AToken = "zRgurs0TqzcAAAAAAAAAAcr7E29CoKWSgsmmZPcso9rwJF8_y5EUrxPf6HONEVds"

cloudStoring = TransferData(access_token)

while(os.path.isfile(file_from) == False):
    fileFrom = input("Enter the file path to transfer:- ")

cloudStoring.upload_file(fileFrom)

print("File had been moved!)")