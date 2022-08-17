import moviepy.editor

# Replace the parameter with the location of the video
video = moviepy.editor.VideoFileClip(r"C:/Users/ghosh/Downloads/STEP BY STEP SURYA NAMASKAR FOR BEGINNERS _ Learn Sun Salutation In 3 Minutes_ Simple Yoga Lessons.mp4")

video.audio.write_audiofile("C:/Users/ghosh/some.wav")


import speech_recognition as sr
from translate import Translator
translator= Translator(to_lang="bn")



# # transcribe audio file                                                         
AUDIO_FILE ="C:/Users/ghosh/some.wav"

texts=''
# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  
        texts= r.recognize_google(audio)
        print(texts)