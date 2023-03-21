#default browser
import os
import subprocess
import webbrowser
from time import sleep
import pyttsx3
import pyautogui

engine = pyttsx3.init()
engine.setProperty('rate', 180)


url_playlist = "https://www.youtube.com/playlist?list=PLWYzwmsMUvFjNHF5LfshndZ5XX8b8l6GM"
url_tw_btc = "https://ru.tradingview.com/chart/WBPF9YtH/?symbol=BINANCE%3ABTCUSDT"

def speaker(text):
    """text playback"""
    engine.say(text)
    engine.runAndWait()

def task_playMusic_defaultBrowser(url_playlist: str = url_playlist):
    """Open PlayList with defaul browser"""
    current_pos = pyautogui.position()
    webbrowser.open(url_playlist)
    sleep(1.5)
    pyautogui.click(x=744, y=344, clicks=1, interval=1, button='left')
    sleep(1.5)
    pyautogui.click(x=1805, y=13, clicks=1, interval=1, button='left')
    pyautogui.moveTo(current_pos)
    
def task_chart__defaultBrowser(url_tw_btc: str=url_tw_btc):
    """Open chart window with defaul browser"""
    webbrowser.open(url_tw_btc)
def task_chart__defaultBrowser1(url_tw_btc: str=url_tw_btc):
    """Open chart window with defaul browser"""
    webbrowser.open(url_tw_btc)
    
def hide_browser_window(): 
    pyautogui.click(x=1805, y=13, clicks=1, interval=1, button='left')

def alt_tab():    
    pyautogui.hotkey('alt','tab')

def launch_rdp():
    subprocess.Popen(r'C:\WINDOWS\system32\mstsc.exe')
    sleep(0.3)
    pyautogui.click(1033,428)

def launch_steam_game():
    os.system('cmd /c "start "steam://rungameid/1938090" "steam://rungameid/1938090"')

def stop_bot():
    quit()

def pc_sleepMode():
    os.system('cmd /c "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"')

def pc_shutdown():
    os.system('cmd /c "shutdown /s /f"')

def sep_words(query):
    word = query.split(" ")
    return word
