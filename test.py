#!/usr/bin/env python3
from miami_api import *


def main():
	# returns list containing all currently open dining locations and their hours
	get_open()

	# returns hours for all dining locations open today
	get_today_hours()

	try:
		import tornado
	except ImportError:
		print('You do not have the required module \'tornado\'.')
		print('Please install it by running')
		print()
		print('pip install tornado')
		print()
		input('Press ENTER to continue.')


if __name__ == '__main__':
	main()
