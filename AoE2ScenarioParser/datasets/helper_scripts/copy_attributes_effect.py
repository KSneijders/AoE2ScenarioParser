import pyautogui
from time import sleep

for x in range(5, 0, -1):
    print(x, end=" ")
    sleep(1)
print("\n")

# Change to 'tabbing mode'
pyautogui.press('tab')
sleep(0.2)

for _ in range(0, 9):
    pyautogui.press('tab')

while True:
    pyautogui.hotkey('shiftleft', 'tab')
    pyautogui.hotkey('shiftleft', 'tab')
    pyautogui.hotkey('shiftleft', 'tab')
    pyautogui.hotkey('shiftleft', 'tab')
    sleep(0.05)
    pyautogui.press('enter')
    sleep(0.05)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')
