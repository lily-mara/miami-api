import json
import time

times = None
with open('times.json', 'r') as json_file:
	times = json.load(json_file)

def main():
	print(inside_time_range(2000, 2200))

def inside_time_range(start, stop):
	"""
	Takes two ints, start and stop times in 24-h style time, returns True if it
	is currently within that time range, false otherwise

	returns: True or False if it is currently inside of the given time range
	"""

	now = int(time.strftime('%H%M'))
	return start < now < stop

def get_open():
	"""
	returns: list of currently open dining locations
	"""
	pass

def get_hours(location):
	"""
	returns: list of hours for given location on current weekday
	"""
	pass

def get_today_hours():
	"""
	returns: JSON data containing hours of every open dining location on
		current weekday
	"""
	pass

if __name__ == '__main__':
	main()
