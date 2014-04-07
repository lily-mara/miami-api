#!/usr/bin/env python3
from miami_api import *


def main():
	#returns the hours for `location` on current weekday
	get_hours('harris')
	
	#returns list containing all currently open dining locations and their hours
	get_open()
	
	#returns hours for all dining locations open today
	get_today_hours()

	try:
		import flask
	except ImportError:
		print('You do not have the required module \'flask\'.')
		print('Please install it by running')
		print()
		print('pip install flask')
		print()
		input('Press ENTER to continue.')


if __name__ == '__main__':
	main()
