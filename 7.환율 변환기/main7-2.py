from currency_converter import CurrencyConverter

cc = CurrencyConverter( "http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip" )
print( cc.convert( 1, "USD", "KRW") )
# 업데이트되는 환율 정보가 실시간 정보가 아니라 차이가 발생함..!!