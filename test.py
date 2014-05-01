#!/usr/bin/env python3
from miami_api import *


def main():
	# returns list containing all currently open dining locations and their hours
	get_open()

	# returns hours for all dining locations open today
	get_today_hours()
	
	# returns info for all instances of CSE 274
	get_classes('CSE', '274')

	try:
		import tornado
	except ImportError:
		print('You do not have the required module \'tornado\'.')
		print('Please install it by running')
		print()
		print('pip install tornado')
		print()
		input('Press ENTER to continue.')
		
	try:
		import requests
	except ImportError:
		print('You do not have the required module \'requests\'.')
		print('Please install it by running')
		print()
		print('pip install requests')
		print()
		input('Press ENTER to continue.')


if __name__ == '__main__':
	main()
