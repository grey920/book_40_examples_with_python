from textwrap import indent
import pyautogui
import pyperclip
import time
import os
import threading

def send_message():
    
    # 10초 후에 send_message를 호출한다. 본인이 본인을 다시 불러오기 때문에 10초마다 실행된다
    threading.Timer( 10, send_message ).start()
    
    # os.chdir( os.path.dirname( os.path.abspath(__file__) ) )
    picPosition = pyautogui.locateOnScreen( '11.오토마우스를 활용한 PC카카오톡 자동화/카카오톡_내 사진1.png',grayscale=True, confidence=.5 )
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
    
    pyperclip.copy("파이썬 자동메시지 테스트" )
    pyautogui.hotkey("command", "v")
    time.sleep( 1 )

    pyautogui.press( "enter" )
    time.sleep( 1 )

    pyautogui.write( ["escape"] )
    time.sleep( 1 )


send_message()
    