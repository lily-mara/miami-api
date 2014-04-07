#!/usr/bin/env python3
import json
import time

locations = None


def inside_time_range(start, stop):
	"""
	Takes two ints, start and stop locations in 24-h style time, returns True
	if it is currently within that time range, false otherwise

	returns: True or False if it is currently inside of the given time range
	"""

	now = int(time.strftime('%H%M'))
	return start <= now <= stop


def get_json_data():
	global locations
	with open('locations.json', 'r') as json_file:
		locations = json.load(json_file)


def get_open():
	"""
	returns: list of currently open dining locations
	"""
	open = []
	for location in locations:
		hours = get_hours(location)
		name = locations[location]['name']
		if hours is not None:
			for start, stop in hours[name]:
				if inside_time_range(start, stop):
					open.append([name, (start, stop)])
	return open


def get_weekday():
	weekdays = ["u", "m", "t", "w", "h", "f", "s"]
	return weekdays[int(time.strftime('%w'))]


def get_hours(location):
	"""
	returns: list of hours for given location on current weekday
	"""
	location = locations[location]
	today = get_weekday()

	for i in location['hours']:
		if today in i:
			hours = location['hours'][i]
			return {location['name']: hours}


def get_hour_string(hours):
	hour_string = ''
	for i in hours:
		hour_string += '-'.join(str(j) for j in i)
		hour_string += ' '
	return hour_string


def get_today_hours():
	"""
	returns: hours of every open dining location on current weekday
	"""
	today_hours = {}
	for location in locations:
		hours = get_hours(location)
		if hours is not None:
			today_hours.update(hours)
	return today_hours


if __name__ == 'miami_api':
	get_json_data()
