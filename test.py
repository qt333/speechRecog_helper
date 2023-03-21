from command_func import *
import subprocess
import words

import pyttsx3

engine = pyttsx3.init()
voive = engine.setProperty('voice',voice[0])
engine.say("не знаю зачем тебе это, но вот что получилось")
engine.runAndWait()
