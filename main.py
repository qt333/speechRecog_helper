from unittest import addModuleCleanup
import speech_recognition as sr

rec = sr.Recognizer()
rec.pause_threshold = 0.8
rec.energy_threshold = 0
rec.phrase_threshold = 0.1
# rec.dynamic_energy_ratio = 0.1


def run_commnad(query):
    print(())

with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic, 0.5)
    audio = rec.listen(mic)
    query = rec.recognize_google(audio_data=audio,language="ru-RU")

print((query))