'''
두 가지 동작이 동시에 실행되는 코드 만들기
* 쓰레드를 독립적으로 동작하도록 설정되어 있기 때문에 ctrl+c 를 해도 메인동작만 종료되고 쓰레드1은 종료되지 않고 계속 실행된다. 
'''
import threading # 쓰레드를 사용하기 위한 threading 모듈
import time

# thread_1의 함수로 1초마다 "쓰레드1 동작"을 출력한다
def thread_1():
    while True:
        print("쓰레드1 동작")
        time.sleep( 1.0 )
        
# 쓰레드 설정
t1 = threading.Thread( target=thread_1 ) # target은 위의 함수명과 같다
# 쓰레드 시작
t1.start()

# 메인코드로 "메인동작"을 2초마다 출력
while True:
    print("메인동작")
    time.sleep( 2.0 )