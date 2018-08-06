#slack apikey = xoxb-311178057142-V3HC36MuChwD55GteB0OD1LJ

import os
import time
import re
from slackclient import SlackClient

autho = 'xoxp-310216681603-311372670919-311479934951-59e057e29dca5f2e1f67df7996a9c01d'
bot_user = 'xoxb-310323930819-2hc8scnIbEILm83WixeIvFBR'
bot_token = 'xoxb-311178057142-FgtxXn4RR9mThhsLG9Q84nuC'
channel_name = "general"

sc = SlackClient(bot_token)
api_call = sc.api_call("im.list")
class push_notification():


	def buy(self,name,amount,usd):
		if sc.rtm_connect():

			message = "%d or $%d of %s was bought" % (amount,usd,name)
			sc.api_call('chat.postMessage',channel = 'tradingbot',text=message,as_user = 'true:')

	def sell(self,name,amount):
		if sc.rtm_connect():

			message = "%d or $%d of %s was sold" % (amount,amount,name)
			sc.api_call('chat.postMessage',channel = 'tradingbot',text=message,as_user = 'true:')


	def error(self,):
		if sc.rtm_connect():
			sc.api_call('chat.postMessage',channel = 'tradingbot',text="Trading bot is currently experiencing issues",as_user = 'true:')
			



	def balance(self,name,balance):
		
		message = "Your balance is: $%d" % (balance)
		if sc.rtm_connect():
			for slack_message in sc.rtm_read():
				if 'channel' in slack_message and 'text' in slack_message and slack_message.get('type') == 'message':
					
					text = slack_message['text']
					channel = slack_message['channel']
					if 'balance' in text.lower():
						sc.api_call('chat.postMessage',channel = channel,text=message,as_user = 'true:')
		else:
			print('connect error')
