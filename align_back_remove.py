from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

try :
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('C:/Users/user/PycharmProjects/pythonProject1/storage.json')
creds = store.get()

if not creds or creds.invalid:
    print("make new storage data file ")
    flow = client.flow_from_clientsecrets('C:/Users/user/PycharmProjects/pythonProject1/client_secret_190082935225-0cn40eev9h8oel1cohli9ke8kjvhc3v3.apps.googleusercontent.com.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) if flags else tools.run(flow, store)

DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

FILES = (
    ('df_train.csv'),
)

folder_id = '1WphV16zk0aVfCV4xG8ejgH1MptrvK6ws'

for file_title in FILES :
    file_name = file_title
    metadata = {'name': 'test1.csv',
                'parents' : [folder_id],
                'mimeType': None
                }

    res = DRIVE.files().create(body=metadata, media_body=file_name).execute()
    if res:
        print('Uploaded "%s" (%s)' % (file_name, res['mimeType']))