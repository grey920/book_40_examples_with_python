''' 파일에서 문자를 읽어 라인별로 한글로 번역하기 '''

from os import linesep
import googletrans

translator = googletrans.Translator()

# 파일을 읽어올 경로 지정
read_file_path="9.영어로된 문서를 한글로 자동번역/영어파일.txt"

with open( read_file_path, 'r' ) as f:
    # 파일에서 라인별로 읽어 readLines에 리스트 형태로 바인딩
    readLines = f.readlines()

# 리스트형태로 저장된 readLines에서 한 줄씩 한글로 변환하여 출력
for lines in readLines:
    result1 = translator.translate( lines, dest='ko' )
    print( result1.text )
