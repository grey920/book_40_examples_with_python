''' 구글에서 자동으로 서울 날씨 검색하는 코드 '''
import pyautogui
import time
import pyperclip


pyautogui.moveTo( -956, 320, 0.2 )
pyautogui.doubleClick()
time.sleep(0.5)

pyperclip.copy("서울 날씨") 
pyautogui.hotkey("command", "v") #윈도우는 'ctrl'이지만 mac은 'command'이다
time.sleep(0.5)

pyautogui.write(["enter"]) 
time.sleep(1)