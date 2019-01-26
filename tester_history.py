import ccxt
import csv
import time as timer

coinbasepro = ccxt.coinbasepro()

symbol = 'ETH/USD'
time = '2018-02-17 00:00:00' #Feb 10, 2018
from_timestamp = coinbasepro.parse8601(time)
#print(coinbasepro.fetch_ohlcv(symbol,'1h', since = from_timestamp,limit = 350))

msec = 1000
minute = 60 * msec
while from_timestamp < coinbasepro.milliseconds():
	source = coinbasepro.fetch_ohlcv(symbol,'5m', since = from_timestamp,limit = 350)
	
	for i in range(len(source)):
		with open('history.csv','a') as lists:
			filewriter = csv.writer(lists,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
			filewriter.writerow(source[i])
		

	else:
		from_timestamp += len(source) * minute * 5
	print(coinbasepro.milliseconds()-from_timestamp)

	timer.sleep(coinbasepro.rateLimit/1000)
			
