# 임의의 숫자 생성 코드
from random import *

random_number = randint( 1, 100 )
# print( random_number )

game_count = 1

# 숫자를 맞춰서 break를 탈 때까지 반복한다
while True:
    try:
    
        # 사용자로부터 숫자 입력 받음
        my_number = int( input("1 ~ 100 사이의 숫자를 입력하세요: " ) )
        
        if my_number > random_number:
            print( "DOWN!" )
        elif my_number < random_number:
            print( "UP!" )
        elif my_number == random_number:
            print( f"축하합니다. {game_count}회 만에 맞췄습니다!!!!! " )
            break # 숫자를 맞춘 경우 반복문을 종료한다
        
        # 시도한 게임 카운트를 +1 한다
        game_count = game_count + 1
    
    # try 문 안의 코드에서 에러가 발생했을 경우 except 문을 실행한다. 이제 문자를 입력해도 예외처리를 하여 종료되지 않게 되었다.
    except Exception as e:
        print( f"exception: {e} -  에러가 발생했습니다. 숫자를 입력하세요. " )