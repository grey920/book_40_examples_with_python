from gtts import gTTS
from playsound import playsound

input = input("나는 누구일까요? 입력해주세요: ")
input_text = f"안녕하세요. 저는 {input}입니다."

# 찾아보니 성우 변경은 불가하지만, 한국어는 남성 성우이고 영어는 여성 성우라고 한다
tts = gTTS( text=input_text, lang='ko' )

tts.save( f"3.텍스트를 음성으로 변환/{input}.mp3" )

# 바로 음성 실행
playsound( f"3.텍스트를 음성으로 변환/{input}.mp3" )
