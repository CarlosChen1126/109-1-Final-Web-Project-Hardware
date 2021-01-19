import pyaudio
from subprocess import call
import speech_recognition as sr
def Speech():
    r = sr.Recognizer()
    r.energy_threshold=4000
    with sr.Microphone(sample_rate = 44100, chunk_size = 512) as source:
        print('listening..')
        audio = r.listen(source)
        print('processing')
        message = (r.recognize_google(audio, language = 'zh-TW', show_all=False))
        print(message)
    return message 

