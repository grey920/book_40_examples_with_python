from gtts import gTTS
from playsound import playsound

# 읽어올 파일의 경로를 바인딩
file_path = "3.텍스트를 음성으로 변환/나의텍스트.txt"

# with는 파일을 열고 종료되면 자동으로 파일을 닫는다.
# 파일을 f 라는 이름으로 오픈한다. 한글로 작성된 파일을 열기 때문에 'rt', encoding='UTF-8' 형식으로 열어 글자가 깨지지 않도록 한다
with open( file_path, 'rt', encoding='UTF-8' ) as f:
    # 파일의 전체 내용을 읽어 read_file 변수에 바인딩
    read_file = f.read()
    
tts = gTTS( text=read_file, lang='ko' )
tts.save( "3.텍스트를 음성으로 변환/나의텍스트.mp3" )