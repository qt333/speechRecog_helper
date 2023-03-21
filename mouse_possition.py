import sys
import time
import pyautogui

while True:
    x, y = pyautogui.position()
    output = f"Pixel color at ({x:>4}, {y:>4})".rjust(5)
    lenght = len(output)
    sys.stdout.write(output)
    sys.stdout.write("\b" * lenght)
    sys.stdout.flush()
    time.sleep(1)



