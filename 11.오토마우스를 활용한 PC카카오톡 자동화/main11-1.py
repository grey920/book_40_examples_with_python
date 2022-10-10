''' 사진에서 좌표 추출하는 코드 만들기
Box(left=103, top=100, width=124, height=73)

일정 시간마다 함수를 동작시킬 때 사용하는 라이브러리
pip install schedule 

* locateOnScreen() 인식이 안될때 ( 계속 None )
-> https://stackoverflow.com/questions/43702511/why-pyautogui-locateonscreen-only-returns-none : 픽셀이 깨져서 이미지를 가져오지 못했으므로 아래 명령어를 실행하여 라이브러리를 설치한다
: pip install opencv-python 
'''
import pyautogui
import os

#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir( os.path.dirname( os.path.abspath(__file__) ) )

picPosition = pyautogui.locateOnScreen('카카오톡_내 사진1.png',grayscale=True, confidence=.5)
print( picPosition )

if picPosition is None:
    picPosition = pyautogui.locateOnScreen( '카카오톡_내 사진2.png',grayscale=True, confidence=.5 )
    print( picPosition )

if picPosition is None:
    picPosition = pyautogui.locateOnScreen( '카카오톡_내 사진3.png',grayscale=True, confidence=.5 )
    print( picPosition )