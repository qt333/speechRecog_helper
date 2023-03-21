import os
import subprocess
import webbrowser
from time import sleep
from numpy import vectorize
import words
import pyautogui
import speech_recognition as sr
from command_func import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

import queue

q = queue.Queue()
# TODO:
# 5. подумать что еще можно заскриптовать полезное #


rec = sr.Recognizer()
rec.pause_threshold = 0.8
rec.energy_threshold = 50
rec.phrase_threshold = 0.25
rec.dynamic_energy_ratio = 3

url_playlist = (
    "https://www.youtube.com/playlist?list=PLWYzwmsMUvFjNHF5LfshndZ5XX8b8l6GM"
)
url_tw_btc = "https://ru.tradingview.com/chart/WBPF9YtH/?symbol=BINANCE%3ABTCUSDT"
url_tw_apt = "https://ru.tradingview.com/chart/WBPF9YtH/?symbol=BINANCE%3AAPTUSDT"


def task_queue():
    ...


def recognizer(data, vectorizer, clf):
    trg = words.TRIGGERS.intersection(data.split())
    if not trg:
        return
    data.replace(list(trg)[0], "")
    text_vector = vectorizer.transform([data]).toarray()[0]
    print(text_vector)
    answer = clf.predict([text_vector])[0]
    print(answer)
    func_name = answer.split()[0]
    print(func_name)
    if func_name == 'task_chart__defaultBrowser1':
        exec(f"{func_name}('{url_tw_apt}')")
        return 
    exec(func_name + "()")
    speaker('Выполнено')


def main():
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))

    del words.data_set
    with sr.Microphone() as mic:
        while True:
            try:
                rec.adjust_for_ambient_noise(mic, 0.5)
                audio = rec.listen(mic)
                data = rec.recognize_google(audio_data=audio, language="ru-RU").lower()
                print('data:',data)
                
                recognizer(data, vectorizer, clf)
                sleep(0.1)
            except Exception as e:
                print(e)
            
    # words_list = sep_words(query)
    # print(words_list)

    # else:
    #     print("NOT FOUND")
    # print("Command successfuly done")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        pass
