'''
외부 IP 알아보기
: 특정 사이트(ipconfig.kr)에 접속해서 내가 연결된 IP 확인하기
'''

import requests # 사이트에 접속하기 위한 모듈
import re # IP주소를 찾기 위한 정규식을 사용하기 위해 필요한 re 모듈

req = requests.get("http://ipconfig.kr")
# 정규식을 사용하여 IP 주소를 가져와 out_addr 변수와 바인딩
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print(out_addr)