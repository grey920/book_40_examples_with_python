''' 마우스 좌표를 출력하는 코드
마우스와 키보드를 자동으로 제어하기 위한 라이브러리 설치
pip install pyautogui 

클립보드에 값을 복사하거나 붙여넣기 용도로 사용하며, pyautogui는 한글이 지원되지 않아 검색에 필요한 한글을 클립보드를 이용하여 사용하기 위해 설치한다
(아나콘다 설치시 기본으로 설치되어 있다)
pip install pyperclip

내 구글 검색창 좌표
Point(x=-783, y=522)
네이버
Point(x=-956, y=320)

* 캡처 
시작점: Point(x=-1319, y=264)
끝점: Point(x=-664, y=910)

* 주소창
Point(x=353, y=86)
'''
import pyautogui
import time

while True:
    print( pyautogui.position() ) # 마우스의 좌표를 출력한다
    time.sleep( 0.1 ) # 0.1초 기다린다