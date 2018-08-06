import ccxt
import csv
import time as timer

gdax = ccxt.gdax()

symbol = 'ETH/USD'
time = '2018-02-17 00:00:00' #Feb 10, 2018
from_timestamp = gdax.parse8601(time)
#print(gdax.fetch_ohlcv(symbol,'1h', since = from_timestamp,limit = 350))

msec = 1000
minute = 60 * msec
while from_timestamp < gdax.milliseconds():
	source = gdax.fetch_ohlcv(symbol,'5m', since = from_timestamp,limit = 350)
	
	for i in range(len(source)):
		with open('history.csv','a') as lists:
			filewriter = csv.writer(lists,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
			filewriter.writerow(source[i])
		

	else:
		from_timestamp += len(source) * minute * 5
	print(gdax.milliseconds()-from_timestamp)

	timer.sleep(gdax.rateLimit/1000)
			
