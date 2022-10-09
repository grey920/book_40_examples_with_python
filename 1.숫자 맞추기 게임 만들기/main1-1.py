# 임의의 숫자 생성 코드
from random import *

random_number = randint( 1, 100 )
# print( random_number )

game_count = 1

# 숫자를 맞춰서 break를 탈 때까지 반복한다
while True:
    
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