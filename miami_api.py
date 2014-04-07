import json
import time

times = None
weekdays = None

def main():
	get_json_data()
	print(get_today_hours())


def inside_time_range(start, stop):
	"""
	Takes two ints, start and stop times in 24-h style time, returns True if it
	is currently within that time range, false otherwise

	returns: True or False if it is currently inside of the given time range
	"""

	now = int(time.strftime('%H%M'))
	return start < now < stop

def get_json_data():
	global times
	global weekdays
	with open('times.json', 'r') as json_file:
		times = json.load(json_file)
	with open('weekdays.json', 'r') as json_file:
		weekdays = json.load(json_file)


def get_open():
	"""
	returns: list of currently open dining locations
	"""
	open = []
	for location in times:
		hours = get_hours(location)
		if hours is not None:
			for start, stop in hours:
				if inside_time_range(start, stop):
					open.append(times[location]['name'])
	return open

def get_weekday():
	return weekdays[time.strftime('%w')]

def get_hours(location):
	"""
	returns: list of hours for given location on current weekday
	"""
	location = times[location]
	today = get_weekday()

	for i in location['hours']:
		if today in i:
			hours = location['hours'][i]
			return hours


def get_hour_string(hours):
	hour_string = ''
	for i in hours:
		hour_string += '-'.join(str(j) for j in i)
		hour_string += ' '
	return hour_string


def get_today_hours():
	"""
	returns: JSON data containing hours of every open dining location on
		current weekday
	"""
	today_hours = {}
	for location in times:
		hours = get_hours(location)
		today_hours.update({times[location]['name']: hours})
	return today_hours


if __name__ == '__main__':
	main()
