''' 좌표를 이용하여 메시지를 자동으로 보내는 코드 '''
import pyautogui
import pyperclip
import time
import os

#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir( os.path.dirname( os.path.abspath(__file__) ) )

picPosition = pyautogui.locateOnScreen('카카오톡_내 사진1.png',grayscale=True, confidence=.5)
print( "1", picPosition )

if picPosition is None:
    picPosition = pyautogui.locateOnScreen( '카카오톡_내 사진2.png',grayscale=True, confidence=.5 )
    print( "2", picPosition )

if picPosition is None:
    picPosition = pyautogui.locateOnScreen( '카카오톡_내 사진3.png',grayscale=True, confidence=.5 )
    print( "3", picPosition )
    

clickPosition = pyautogui.center( picPosition )
pyautogui.click( clickPosition )
pyautogui.press( "enter" )

pyperclip.copy("이 메세지는 자동으로 보내는 메세지 입니다!")
pyautogui.hotkey("command", "v")
time.sleep( 1 )

pyautogui.press( "enter" )
time.sleep( 1 )

pyautogui.write( ["escape"] )
time.sleep( 1 )