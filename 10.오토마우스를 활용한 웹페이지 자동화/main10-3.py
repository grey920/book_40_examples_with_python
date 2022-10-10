''' 서울 날씨 화면 자동 캡처 후 저장하는 코드 '''

import pyautogui
import time
import pyperclip


pyautogui.moveTo( 550, 260, 0.2 )
pyautogui.doubleClick()
time.sleep(0.5)

pyperclip.copy("서울 날씨") 
pyautogui.hotkey("command", "v") #윈도우는 'ctrl'이지만 mac은 'command'이다
time.sleep(0.5)

pyautogui.write(["enter"]) 
time.sleep(1)


start_x = 43
start_y = 384
end_x = 689
end_y = 938

pyautogui.screenshot( '10.오토마우스를 활용한 웹페이지 자동화/서울날씨.png', region=( start_x, start_y, end_x-start_x, end_y-start_y ) )
