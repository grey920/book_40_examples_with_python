import qrcode

file_path = "4.QR코드 생성기/qr코드모음.txt"

with open( file_path, 'rt', encoding='UTF-8' ) as f:
    # readlines(): 파일을 읽어 라인 별로 리스트의 값의 형태로 내어준다.
    read_lines = f.readlines()
    
    for line in read_lines:
        # line.strip(): 줄 마지막에 줄바꿈 문자를 삭제한다
        line = line.strip()
        print( line )
        
        #
        qr_data = line
        qr_img = qrcode.make( qr_data )
        
        save_path = "4.QR코드 생성기/" + qr_data.replace( "/", ".") + ".png"
        qr_img.save( save_path )