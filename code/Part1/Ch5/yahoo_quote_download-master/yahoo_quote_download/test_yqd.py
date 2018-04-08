# -*- coding: utf-8 -*-
"""
Created on Sat May 20 18:58:59 2017

@author: c0redumb
"""

import yqd
import pandas as pd
def load_quote(ticker):
	# open('foo.csv','w').write(yqd.load_yahoo_quote(ticker, '20170515', '20170517'))
	print('===', ticker, '===')
	data = []
	data  = yqd.load_yahoo_quote(ticker, '20000101', '20170517')
	my_df = pd.DataFrame(data[1:])
	my_df.to_csv('foo.csv', index=False)
	print(data[1:])
	# print(data.Volume)
	# print(yqd.load_yahoo_quote(ticker, '20170515', '20170517', 'dividend'))
	# print(yqd.load_yahoo_quote(ticker, '20170515', '20170517', 'split'))

def test():
	# Download quote for stocks
	load_quote('GOOGL')
	# load_quote('C')

	# Download quote for index
	# load_quote('^DJI')

if __name__ == '__main__':
	test()
