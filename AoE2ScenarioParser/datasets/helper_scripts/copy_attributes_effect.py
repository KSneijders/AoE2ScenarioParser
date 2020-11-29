from time import sleep

import pyautogui

for x in range(5, 0, -1):
    print(x, end=" ")
    sleep(1)
print("\n")

# Change to 'tabbing mode'
pyautogui.press('tab')
sleep(0.2)

tabs_from_copy_to_list = 10

for _ in range(tabs_from_copy_to_list + 5):
    pyautogui.press('tab')

while True:
    for _ in range(tabs_from_copy_to_list):
        pyautogui.hotkey('shiftleft', 'tab')
    sleep(0.05)
    pyautogui.press('enter')
    sleep(0.05)
    for _ in range(tabs_from_copy_to_list):
        pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')
