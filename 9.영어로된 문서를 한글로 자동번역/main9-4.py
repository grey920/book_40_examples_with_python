from os import linesep
import googletrans

translator = googletrans.Translator()

# 파일을 읽어올 경로 지정
read_file_path="9.영어로된 문서를 한글로 자동번역/영어파일.txt"
write_file_path="9.영어로된 문서를 한글로 자동번역/한글파일.txt"

with open( read_file_path, 'r' ) as f:
    # 파일에서 라인별로 읽어 readLines에 리스트 형태로 바인딩
    readLines = f.readlines()

# 리스트형태로 저장된 readLines에서 한 줄씩 한글로 변환하여 출력
for lines in readLines:
    result1 = translator.translate( lines, dest='ko' )
    print( result1.text )
    # 'a' 옵션: 쓰기 모드. w옵션과 달리 이미 파일이 존재하면 그 파일의 끝으로 커서가 가고, 그 뒤에 이어쓴다
    with open( write_file_path, 'a', encoding='UTF-8') as f:
        f.write( result1.text + '\n' )
