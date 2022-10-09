'''
메인코드가 동작할 때에만 쓰레드 동작하는 코드 만들기
이제 ctrl+c를 하면 한번에 두 쓰레드 모두 종료된다

* 데몬 쓰레드: 백그라운드에서 실행되는 쓰레드로 일반 쓰레드를 보조하는 역할을 하는 쓰레드. 데몬 쓰레드는 메인 쓰레드가 종료되면 그 즉시 종료된다
'''
import threading # 쓰레드를 사용하기 위한 threading 모듈
import time

def thread_1():
    while True:
        print("쓰레드1 동작")
        time.sleep( 1.0 )
        
t1 = threading.Thread( target=thread_1 )
t1.daemon = True # 쓰레드를 데몬쓰레드로 설정하여 메인동작이 실행될 때에만 쓰레드를 실행하도록 함
t1.start()

while True:
    print("메인동작")
    time.sleep( 2.0 )