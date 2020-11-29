from time import sleep
from tkinter import Tk

import pyautogui

r = Tk()

"""
When copying select the top entry. With Units and Buildings this'll be '<none>'. For technologies this isn't the case. 
So just select the top Technology.

For units/buildings: Use 'Create Object'
For Technologies: Use 'Enable/Disable Technology'
"""
copying_techs = False


def copy_and_print(last=""):
    pyautogui.hotkey('ctrl', 'c')
    obj_id = r.selection_get(selection="CLIPBOARD")
    a = check_if_duplicate(obj_id, last)
    print(obj_id)
    return a


def check_if_duplicate(new, last):
    if new == last:
        exit("Same ID twice. End reached")
    else:
        return new


for x in range(5, 0, -1):
    print(x, end=" ")
    sleep(1)
print("\n")

# Change to 'tabbing mode'
pyautogui.press('tab')
sleep(0.2)

last_obj_id = ""

if copying_techs:
    pyautogui.hotkey('shiftleft', 'tab')
    sleep(0.05)
    pyautogui.press('enter')
    sleep(0.05)
    pyautogui.press('enter')
    sleep(0.05)
    pyautogui.press('tab')
    copy_and_print()

while True:
    # Move to dropdown
    pyautogui.hotkey('shiftleft', 'tab')
    if not copying_techs:
        pyautogui.hotkey('shiftleft', 'tab')
    sleep(0.05)

    # Open dropdown
    pyautogui.press('enter')
    sleep(0.05)

    # Next unit
    pyautogui.press('down')
    sleep(0.05)

    # Select unit
    pyautogui.press('enter')
    sleep(0.05)

    # Move to ID field
    pyautogui.press('tab')
    if not copying_techs:
        pyautogui.press('tab')
    sleep(0.05)

    last_obj_id = copy_and_print(last=last_obj_id)
