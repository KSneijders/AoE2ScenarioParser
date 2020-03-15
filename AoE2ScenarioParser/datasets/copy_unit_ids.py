import pyautogui
from time import sleep
from tkinter import Tk
r = Tk()

sleep(5)

# Change to 'tabbing mode'
pyautogui.press('tab')

last_obj_id = ""

while True:
    sleep(0.2)
    # Move to dropdown
    pyautogui.hotkey('shiftleft', 'tab')
    pyautogui.hotkey('shiftleft', 'tab')
    sleep(0.2)
    # Open dropdown
    pyautogui.press('enter')
    sleep(0.2)
    # Next unit
    pyautogui.press('down')
    sleep(0.2)
    # Select unit
    pyautogui.press('enter')
    sleep(0.5)
    # Move to ID field
    pyautogui.press('tab')
    pyautogui.press('tab')
    sleep(0.2)
    # Copy
    pyautogui.hotkey('ctrl', 'c')
    obj_id = r.selection_get(selection="CLIPBOARD")

    if obj_id == last_obj_id:
        exit("Same ID twice. End reached")
    else:
        last_obj_id = obj_id
    print(obj_id)
