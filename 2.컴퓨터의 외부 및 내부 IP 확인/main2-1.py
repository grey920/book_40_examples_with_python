'''
집주소를 아파트로 본다면, 외부 IP는 XX시 XX동 XX아파트이다. 내부 IP는 동의 호수로 볼 수 있다. 
일반적으로 인터넷 망이 설치된 가정집에는 공유기가 있어 여러 대의 컴퓨터, 스마트폰, TV 등의 기기를 연결하여 사용한다.

내부 IP: 집에 있는 공유기가 주소를 할당한다. 집 안의 컴퓨터, 스마트폰, TV 등의 기기를 연결할 수 있게되는 것이다. 
외부 IP: KT, LG 등 인터넷 망 공급자가 주소를 할당한다. 

'''
# 컴퓨터가 연결된 접속정보를 받아올 때 사용하는 모듈
import socket

# 연결된 소켓의 이름을 가져와 in_addr 변수와 바인딩
in_addr = socket.gethostbyname( socket.gethostname() )

# in_addr을 출력하여 내부 IP 확인
print( in_addr )


print( "hostname: ", socket.gethostname() )
print( "ip address: ", socket.gethostbyname( socket.gethostname() ))

naver_domain = "www.naver.com"
print( "ip address of naver : ", socket.gethostbyname( naver_domain ) )