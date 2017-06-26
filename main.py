from pydub import AudioSegment


sound = AudioSegment.from_mp3("C:\Users\emmet\Desktop\make.mp3")

# len() and slicing are in milliseconds
halfway_point = len(sound) / 2

ten_seconds = 10 * 1000

second_half = sound[halfway_point:]

audio_clip = second_half[:ten_seconds]


# writing mp3 files is a one liner
audio_clip.export("C:\Users\emmet\Desktop\Export\make.mp3", format="mp3")