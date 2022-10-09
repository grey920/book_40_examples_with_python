
import itertools
import zipfile


# 숫자, 영문 소문자/대문자 문자열을 변수에 바인딩
passwd_string = "012345789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 암호가 걸린 zip파일 경로
zFile = zipfile.ZipFile("./암호1234.zip")

for len in range( 1, 6 ): # 1 ~ 5까지 반복
    # passwd_string의 모든 문자열을 repeat=길이 로 정렬하여 변환
    to_attempt = itertools.product( passwd_string, repeat= len )
    
    # 정렬하여 변환된 수만큼 반복한다
    for attempt in to_attempt:
        # 리스트로 반환된 값을 문자열로 변환한다. ''.join( 리스트 )는 리스트의 값을 문자열로 변환한다
        passwd = ''.join( attempt )
        print( passwd )
        
        # 비밀번호를 입력해서 맞으면 try, 틀리면 except를 실행한다
        try:
            zFile.extractall( pwd=passwd.encode() ) # 비밀번호를 입력한다. 
            print(f"비밀번호는 {passwd} 입니다")
            break
        except:
            pass