import moviepy.editor
from playsound import playsound


# Replace the parameter with the location of the video
video = moviepy.editor.VideoFileClip(r"C:/Users/ghosh/Downloads/studyiq.mp4")

video.audio.write_audiofile("C:/Users/ghosh/some.wav")



# # transcribe audio file                                                       
AUDIO_FILE ="C:/Users/ghosh/some.wav"

##Playsound module of 1.2.2 version only able to play music in wav format  
# playsound(AUDIO_FILE)
import speech_recognition as sr
# from translate import Translator
# translator= Translator(to_lang="bn")


#use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        # read the entire audio file    
        audio = r.record(source)               
        texts= r.recognize_google(audio,language="en-US")
        print(texts)
        
        
        
        