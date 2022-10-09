'''
* Mac OS에서 압축시 암호 걸기 ( https://zzsza.github.io/development/2019/05/08/mac-zip-password/ )
1. 터미널에서 zip 명령어로 -e 옵션을 걸어 압축한다
형식) zip -e [압축된파일명.zip] [압축할 파일명] 
예) zip -e 암호1234.zip 암호1234.txt 
2. 명령어를 실행하면 Enter password: 가 나오고 암호를 입력한다
'''
import itertools

# 문자열을 순서대로 배열

# 숫자, 영문 소문자/대문자 문자열을 변수에 바인딩
passwd_string = "012345789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for len in range( 1, 4 ): # 1 ~ 3까지 반복
    # passwd_string의 모든 문자열을 repear=길이 로 정렬하여 변환
    to_attempt = itertools.product( passwd_string, repeat= len )
    
    # 정렬하여 변환된 수만큼 반복한다
    for attempt in to_attempt:
        # 리스트로 반환된 값을 문자열로 변환한다. ''.join( 리스트 )는 리스트의 값을 문자열로 변환한다
        passwd = ''.join( attempt )
        print( passwd )