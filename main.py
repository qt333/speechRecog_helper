from operator import le
from socket import if_nameindex
from time import sleep
import speech_recognition as sr

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import webbrowser 
import subprocess
import os


#TODO: 
# 1.завернуть вся функ в отдельный файл
# 2.добавить векторазед метод определения комманды
# 3. завернуть комманды в дикшенери как в https://www.youtube.com/watch?v=MXdsPKZyZ48&t=1205s 
# 4. не забывать коммиты и пуш в репу!
# 5. подумать что еще можно заскриптовать полезное #


rec = sr.Recognizer()
rec.pause_threshold = 0.5
rec.energy_threshold = 300
rec.phrase_threshold = 0.25
rec.dynamic_energy_ratio = 3
url_playlist = "https://www.youtube.com/playlist?list=PLWYzwmsMUvFjNHF5LfshndZ5XX8b8l6GM"
url_tw_btc = "https://ru.tradingview.com/chart/WBPF9YtH/?symbol=BINANCE%3ABTCUSDT"

#default browser
def task_playMusic_defaultBrowser():
    webbrowser.open(url_playlist)
    sleep(1.2)
    pyautogui.click(x=744, y=344, clicks=1, interval=1, button='left')
    sleep(1.2)
    pyautogui.click(x=1805, y=13, clicks=1, interval=1, button='left')
    
def task_chart__defaultBrowser():
    webbrowser.open(url_tw_btc)
    
def hide_browser_window(): 
    pyautogui.click(x=1805, y=13, clicks=1, interval=1, button='left')

def alt_tab():    
    pyautogui.hotkey('alt','tab')

def launch_rdp():
    subprocess.Popen(r'C:\WINDOWS\system32\mstsc.exe')
    sleep(0.2)
    pyautogui.click(1033,428)

def stop_bot():
    quit()

def pc_sleepMode():
    #попытка через хоткей
    # pyautogui.hotkey('alt','f4')
    # sleep(0.4)
    # pyautogui.press('up')
    os.system('cmd /c "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"')

def pc_shutdown():
    os.system('cmd /c "shutdown /s /f"')

#selenium
# def task_playMusic():
#     options = Options()
#     options.page_load_strategy = "none"
#     options.headless = False
#     options.add_argument(
#         "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
#     )
#     options.add_extension(r'C:\Users\QUOTAAAA\Python_test_bince\speechRecog_helper\AdBlock-—.crx')
#     # Here Chrome  will be used
#     driver = webdriver.Chrome(options=options)
#     driver.maximize_window()
    
#     # URL of website
#     driver.get(
#         url_playlist
#     )
#     sleep(5)
#     actions = ActionChains(driver)
#     actions.move_by_offset(744,218).click().perform()
#     print('после клика')
#     x, y = pyautogui.position()
#     output = f"Pixel color at ({x:>4}, {y:>4})".rjust(5)
#     print(x,y)
    
#     sleep(30)
#     driver.quit()

def sep_words(query):
    word = query.split(" ")
    return word

def main():
    
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic, 0.5)
        audio = rec.listen(mic)
        query = rec.recognize_google(audio_data=audio, language="ru-RU").lower()
    
    words_list = sep_words(query)
    print(words_list)
    if "запусти" in words_list and "музыку" in words_list:
        # task_playMusic()
        task_playMusic_defaultBrowser()
    elif "запусти" in words_list and "график" in words_list:
        task_chart__defaultBrowser()
    elif "скрыть" in words_list or "вкладку" in words_list:
        hide_browser_window()
    elif "tab" in words_list or "табуляция" in words_list or 'овуляция' in words_list:
        alt_tab()
    elif "удалённый" in words_list and "комп" in words_list or 'рдп' in words_list:
        launch_rdp()
    elif "выключись" in words_list and "бот" in words_list or 'выключить' in words_list and 'бота' in words_list:
        stop_bot()
    elif "слип" in words_list and "мод" in words_list or 'режим' in words_list and 'сна' in words_list\
        or 'sleep' in words_list and 'mode' in words_list:
        pc_sleepMode()
    elif "завершение" in words_list and "работы" in words_list or 'завершить' in words_list\
        and 'работу' in words_list:
        pc_shutdown()
    else:
        print("NOT FOUND")
    print("Command successfuly done")

if __name__ == "__main__":
    while 1:
        try:
            main()
        except Exception as e:
            print(e)
            sleep(0.1)
            pass
        