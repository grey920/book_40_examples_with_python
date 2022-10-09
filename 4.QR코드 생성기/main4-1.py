'''
QR코드 생성 코드 만들기

qr코드 생성기는 단순하게 문자를 qr코드로 변환하기 때문에 어떠한 문자라도 가능하다
'''

import qrcode

qr_data = "www.naver.com"

# qrcode.make()로 이미지를 만들어 qr_img에 바인딩
qr_img = qrcode.make( qr_data )

# qr 이미지를 저장할 파일 경로
save_path = "4.QR코드 생성기/" + qr_data + ".png"

# 이미지를 경로에 저장
qr_img.save( save_path )