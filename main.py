# -*- coding: utf-8 -*-
from twython import Twython
from printer import Printer
import unicodedata
import time

class Microprinter:
	def __init__(self):
		self.twitter = Twython()
		self.twitterQuery = ''
		self.last_id = 0
		self.printer = Printer('\\\\.\\CNCB0')

	def __deaccent(self, text):
		return ''.join(char
		for char in unicodedata.normalize('NFD', text)
		if not unicodedata.combining(char)
		)

	def twitterParse(self):
		searchResults = self.twitter.search(q=self.twitterQuery)
		items = reversed(searchResults['results'])

		for item in items:
			id = time.strftime('%Y%m%d%H%M',
							   time.strptime(item['created_at'].encode('utf-8'), '%a, %d %b %Y %H:%M:%S +0000'))
			id = int(id)

			if id > self.last_id:
				text = self.__deaccent(item['text']).encode('ascii')
				user = ''
				user_name = self.__deaccent(item['from_user']).encode('ascii')
				real_name = self.__deaccent(item['from_user_name']).encode('ascii')

				if real_name == None:
					user = user_name
				else:
					user = user_name + ' (' + real_name + ')'

				self.printer.writeln(text)
				self.printer.writeln('user: ' + user)
				self.printer.center()
				self.printer.writeln('-----------------------------------------------')
				self.printer.left()
				self.printer.writeln("")

				print(text)
				print('user: ' + user)
				print('-----------------------------------------------')

				self.last_id = id


mp = Microprinter()
mp.twitterQuery = '#brmlab OR @brmlab'

while True:
	mp.twitterParse()

	time.sleep(60)