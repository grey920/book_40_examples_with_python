'''
환율 계산을 위한 currencyconverter 라이브러리 설치
pip install currencyconverter
'''

from currency_converter import CurrencyConverter

cc = CurrencyConverter()
print( cc.currencies ) # 지원되는 통화 목록 출력