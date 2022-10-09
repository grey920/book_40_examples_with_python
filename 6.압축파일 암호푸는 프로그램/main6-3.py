'''
비밀번호를 찾으면 프로그램이 종료되는 코드 만들기
'''
import itertools
import zipfile

def un_zip( passwd_string, min_len, max_len, zFile ):
    # for len in range( min_len, max_len + 1 ): 
    for len in range( 4,5 ): 
        to_attempt = itertools.product( passwd_string, repeat= len ) # https://docs.python.org/ko/3/library/itertools.html
    
        for attempt in to_attempt:
            passwd = ''.join( attempt )
            print( passwd )
            
            try:
                # extractall() : 모든 파일 압축해제. 경로를 지정하지 않으면 현재 작업디렉토리에 바로 압축이 해제된다
                zFile.extractall( pwd=passwd.encode() ) 
                print(f"비밀번호는 {passwd} 입니다")
                return 1
            except:
                pass
            


passwd_string = "012345789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zFile = zipfile.ZipFile("./암호1234.zip")

min_len = 1
max_len = 5

unzip_result = un_zip( passwd_string, min_len, max_len, zFile )

if unzip_result == 1:
    print( "암호 찾기에 성공했습니다.")
else:
    print( "암호찾기 실패...")