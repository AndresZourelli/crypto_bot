
import ccxt  # noqa: E402




class account():

	def __init__(self):
		self.gdax = ccxt.gdax()
		self.gdax  = ccxt.gdax({
    	'apiKey': "0e1354dd982e3469614e973122489b04",
    	'secret': "BlZ5JHt1rC6phWO2ZHWuPrHORv08r3ZCdH46f126OzdwRS+ze7P/CmW/NMbSvurV0EWGu/AyHhFR9Ou1BIf9Kw==",
    	'password': 'pw4vlmk5u9',
    	'verbose': False,  # switch it to False if you don't want the HTTP log
		})
	def my_order(self,name):
		return self.gdax.fetchTrades(name)

	def order_id(self,order):
		return self.gdax.parse_order(order)

	
	def order(self,name):
		return self.gdax.fetchOpenOrders(symbol = name)


	def buy(self, close):
		buy_amount = 0
		account_USD = self.gdax.fetch_balance()['free']['USD']

		if account_USD < 5:
			buy_amount = 0
		else:
			buy_amount = round(.80*(account_USD/close),8)

		return self.gdax.create_market_buy_order('ETH/USD', buy_amount)

	def sell(self,close):
		account_ETH = self.gdax.fetch_balance()['free']['ETH']
		if account_ETH >= 0.01:
			return self.gdax.create_market_sell_order('ETH/USD',  round(account_ETH,8))
		else:
			print('Cannot Place Order, Minimun must be 0.01 ETH')

		
		

	def balance_USD(self,ticks):
		account_USD = self.gdax.fetch_balance()['free']['USD']
		account_ETH = self.gdax.fetch_balance()['free']['ETH']
		total = account_ETH*ticks + account_USD
		return total




