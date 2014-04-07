from miami_api import *


def main():
	#returns the hours for `location` on current weekday
	get_hours('harris')
	
	#returns list containing all currently open dining locations and their hours
	get_open()
	
	#returns hours for all dining locations open today
	get_today_hours()


if __name__ == '__main__':
	main()
