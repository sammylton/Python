# This script sends the "Block me permanently!" message to a person on my WhatsApp. The web WhatsApp window(or the browser) should not be minimized.
# Compilation: > python sendwhatsapp.py
# Before compilation, you need the following packages, for which you need to run the following commands:
# sudo apt install python3-pip
# pip install pywhatkit
# sudo apt-get install python3-tk python3-dev (NOTE: You must install tkinter on Linux to use MouseInfo. Run this command.)
# pip install keyboard
# pip install pyautogui
# pip install time 
import time
import pywhatkit
import pyautogui
from tkinter import *
from datetime import datetime

win = Tk()
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
count = 0

while count <= 100:
    now = datetime.now()
    current_hour = now.hour
    current_minute = now.minute

    # Send the message
    pywhatkit.sendwhatmsg("+916378175194", "Block me permanently!", current_hour, current_minute + 1, 15)

    # Press the Enter key after sending the control to the WhatsApp window (should not be minimized) 
    pyautogui.moveTo(screen_width * 0.694, screen_height * 0.964)
    pyautogui.click()
    pyautogui.press('enter')

    # Add delay to ensure the message is sent before closing the tab
    time.sleep(2)

    # Close the tab
    pyautogui.hotkey('ctrl', 'w')

    # Move to the next iteration of the loop
    count = count + 1
