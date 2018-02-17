import glob
import os
from pydub import AudioSegment
import uuid
import boto
from ctypes import *

os.chdir("C:/Users/emmet/Desktop/TestTracks")
for file in glob.glob("*.mp3"):
    sound = AudioSegment.from_mp3(file)
    halfway_point = len(sound) / 2
    ten_seconds = 5 * 1000
    second_half = sound[halfway_point:]
    audio_clip = second_half[:ten_seconds]
    audio_clip = audio_clip.fade_in(500).fade_out(500)
    folderDestination = "C:/Users/emmet/Desktop/TestOutput/"
    filename = os.path.basename(file)
    filename = filename.replace(" ", "")
    final = folderDestination + filename
    audio_clip.export(final, format="mp3")
