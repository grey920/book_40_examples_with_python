'''
실시간 환율 정보 크롤링
'''
import requests
from bs4 import BeautifulSoup


def get_exchange_rate( target1, target2 ):
    # 아무런 헤더 없이 접속하면 로봇이 접속한 것으로 보여 사이트에서 정보를 내주지 않는다...!! 일반적인 브라우저를 이용하여 접속한 것처럼 보이게 한다
    headers = {
        "User-Agent" : "Mozilla/5.0",
        "Content-Type" : "text/html; charset=utf-8"
    }
    
    # requests 라이브러리를 이용하여 사이트에 접속하여 응답값을 가져온다
    response = requests.get( "https://kr.investing.com/currencies/{}-{}".format(target1, target2), headers=headers )
    # BeautifulSoup을 이용하여 html로 보기 값을 찾기 좋게 한다
    content = BeautifulSoup( response.content, "html.parser" )
    # 마지막 환율 정보 찾기
    containers = content.find('span', {'data-test': 'instrument-price-last'})
    print( containers.text )



get_exchange_rate( 'usd', 'krw' )