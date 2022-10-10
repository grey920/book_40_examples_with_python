''' 일정 간격마다 보내는 코드 '''

import pyautogui
import pyperclip
import time
import schedule

def send_message():
    
    picPosition = pyautogui.locateOnScreen( '11.오토마우스를 활용한 PC카카오톡 자동화/카카오톡_내 사진1.png',grayscale=True, confidence=.5 )
    print( "1", picPosition )
    
    if picPosition is None:
        picPosition = pyautogui.locateOnScreen( '11.오토마우스를 활용한 PC카카오톡 자동화/카카오톡_내 사진2.png',grayscale=True, confidence=.5 )
        print( "2", picPosition )

    if picPosition is None:
        picPosition = pyautogui.locateOnScreen( '11.오토마우스를 활용한 PC카카오톡 자동화/카카오톡_내 사진3.png',grayscale=True, confidence=.5 )
        print( "3", picPosition )
        
    
    clickPosition = pyautogui.center( picPosition )
    pyautogui.click( clickPosition )
    pyautogui.press( "enter" )
    
    pyperclip.copy("파이썬 자동메시지 테스트 - 매 정각에 전송" )
    pyautogui.hotkey("command", "v")
    time.sleep( 1 )

    pyautogui.press( "enter" )
    time.sleep( 1 )

    pyautogui.write( ["escape"] )
    time.sleep( 1 )


# 10초마다 send_message()를 실행할 스케쥴을 등록한다
# schedule.every( 10 ).seconds.do( send_message )
schedule.every().hour.at(":10").do( send_message )

while True:
    # pending() : 계속 실행되면서 스케줄에 등록된 함수를 설정된 시간마다 실행한다
    schedule.run_pending()
    time.sleep( 1 )