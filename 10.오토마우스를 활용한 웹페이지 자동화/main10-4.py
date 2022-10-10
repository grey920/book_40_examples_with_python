
import pyautogui
import time
import pyperclip

weatherList = [ "서울 날씨", "대전 날씨", "청주 날씨", "부산 날씨", "제주도 날씨" ]

# 주소창 좌표
addr_x = 353
addr_y = 86
# 스크린샷 좌표
start_x = 43
start_y = 384
end_x = 689
end_y = 938


for weather in weatherList:
    # 주소창으로 이동
    pyautogui.moveTo( addr_x, addr_y, 1 )
    time.sleep( 0.2 )
    pyautogui.doubleClick()
    time.sleep( 0.2 )
    # 주소창 초기화
    pyautogui.hotkey("command", "a")
    pyautogui.press( "delete" )
    
    # 네이버로 이동
    pyperclip.copy( "www.naver.com" ) # 왜인지 모르겠으나 pyautogui.write()로 입력하면 컴퓨터가 엉뚱한 동작을 함..
    pyautogui.hotkey("command", "v")
    pyautogui.press( "enter" )
    time.sleep( 1 )
    
    # 네이버 검색창으로 이동
    pyautogui.moveTo( 550, 260, 0.2 )
    pyautogui.doubleClick()
    time.sleep(0.5)

    # 검색할 지역 날씨 이름을 클립보드에 저장
    pyperclip.copy( weather )
    print( weather )
    pyautogui.hotkey("command", "v")
    time.sleep(0.5)
    pyautogui.write(["enter"]) # 지역날씨 검색
    time.sleep(1)
    
    # 저장될 스크린샷 경로
    img_path = f'10.오토마우스를 활용한 웹페이지 자동화/{ weather }.png'
    
    # 지정된 스크린샷 좌표대로 이미지 저장
    pyautogui.screenshot( img_path , region=( start_x, start_y, end_x-start_x, end_y-start_y ) )

