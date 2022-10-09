''' 
좀 더 정확하게 내부 IP 확인하기 

* socket: 네트워크에서 패킷을 주고 받을 때 각 end 단에서 application으로 넘어가기전에 받는 버퍼같은 것.

'''
import socket

# 소켓 연결 ( https://docs.python.org/ko/3/library/socket.html ). 
# (패밀리) socket.AF_INET: 해당 소켓을 IP version 4 용으로 사용하겠다는 의미
# (타입) socket.SOCK_STREAM: 해당 소켓에 TCP 패킷을 받겠다는 의미
in_addr = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) 

# 클라이언트가 서버에 연결하기 - connect(). 클라이언트는 능동적으로 서버에 연결하며, 연결된 소켓으로 항상 1:!로 통신하기 때문에 서버처럼 bind나 listening 과정이 필요없다. 
# 구글에 https 기본 포트인 443 포트로 접속한다.
in_addr.connect( ( "www.google.co.kr", 443 ) )

# socket.getsockname(): 소켓 자신의 주소를 반환.
# 연결된 소켓의 이름을 출력
print( in_addr.getsockname()[0] )