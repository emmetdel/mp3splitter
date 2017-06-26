# import glob
# import os
# from pydub import AudioSegment
# import uuid
# from google.cloud import datastore
# # import gcs_oauth2_boto_plugin
# import boto
from ctypes import *


# project_id = 'tracksniffer1'
# datastore_client = datastore.Client(project_id, "TrackSnifferDb")
# kind = 'SongClip'
# GOOGLE_STORAGE = 'gs'
# bucket_name = kind

# Instantiate a BucketStorageUri object.
# uri = boto.storage_uri(bucket_name, GOOGLE_STORAGE)

#Try to create the bucket.
# try:
#     # If the default project is defined,
#     # you do not need the headers.
#     # Just call: uri.create_bucket()
#     header_values = {"x-goog-project-id": 175709600196}
#     uri.create_bucket(headers=header_values)

# except:
#     print ('Failed to create bucket:')

lib = cdll.LoadLibrary("/go/main.so")
lib.Add.argtypes = [c_longlong, c_longlong]
print ("awesome.Add(12,99) = %d" % lib.Add(12,99))

# os.chdir("C:/Users/emmet/Desktop/TestTracks")
# for file in glob.glob("*.mp3"):
#     sound = AudioSegment.from_mp3(file)
#     halfway_point = len(sound) / 2
#     ten_seconds = 5 * 1000
#     second_half = sound[halfway_point:]
#     audio_clip = second_half[:ten_seconds]
#     audio_clip = audio_clip.fade_in(500).fade_out(500)
#     folderDestination = "C:/Users/emmet/Desktop/TestOutput/"
#     filename = os.path.basename(file)
#     filename = filename.replace(" ", "")
#     final = folderDestination + filename
#     audio_clip.export(final, format="mp3")

#     # dst_uri = boto.storage_uri(bucket_name + '/' + filename, GOOGLE_STORAGE)
#     # dst_uri.new_key().set_contents_from_file(file)


#     # The name/ID for the new entity
#     uniqueIdentifier = str(uuid.uuid4())

#     name = filename
#     # The Cloud Datastore key for the new entity
#     task_key = datastore_client.key(kind, uniqueIdentifier)
#     task = datastore.Entity(key=task_key)
#     task['SongClipName'] = name

#     # Saves the entity
#     datastore_client.put(task)