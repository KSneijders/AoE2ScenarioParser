from time import sleep

import pyautogui

# [Condition] Accumulate Attribute
# distance_to_list = 9
# distance_to_copy = 4

for x in range(5, 0, -1):
    print(x, end=" ")
    sleep(1)
print("\n")

# Change to 'tabbing mode'
pyautogui.press('tab')
sleep(0.2)

for _ in range(0, 12):
    pyautogui.press('tab')

while True:
    pyautogui.press('tab')
    pyautogui.hotkey('shiftleft', 'tab')
    pyautogui.hotkey('shiftleft', 'tab')

    pyautogui.press(['1', '0'])

    for _ in range(0, 25):
        pyautogui.hotkey('tab')
    sleep(0.05)
    pyautogui.press('enter')
    sleep(0.05)
    for _ in range(0, 7):
        pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')
