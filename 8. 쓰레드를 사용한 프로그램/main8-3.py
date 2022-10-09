'''
다수의 쓰레드를 동작시키는 코드

1번 쓰레드, 2번 쓰레드, 메인쓰레드가 모두 경쟁적으로 실행하고 종료한다
'''
import threading

def sum( name, value ):
    for i in range( 0, value ):
        print( f"{name} : {i}")

t1 = threading.Thread( target=sum, args=("1번 쓰레드", 10 ) )
t2 = threading.Thread( target=sum, args=("2번 쓰레드", 10 ) )

t1.start()
# t2.daemon= True -> t2를 데몬쓰레드로 설정해보니 "_enter_buffered_busy: could not acquire lock for <_io.BufferedWriter name='<stdout>'> at interpreter shutdown, possibly due to daemon threads" 에러가 종종 발생
t2.start()

print("Main Thread")