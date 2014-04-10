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
	hours = []
	for location in locations:
		location_time = get_status(location)
		if location_time is not None:
			if location_time['is_open']:
				hours.append(location_time)

	for location in hours:
		id = location['id']
		name = location['name']
		for times in location['hours']:
			if times['is_open']:
				open_time = times['open']
				close_time = times['close']
				open.append({
					'name': name,
					'open': open_time,
					'close': close_time
					})
	open = sorted(open, key=lambda x: x['close'])
	return open


def get_weekday():
	weekdays = ["u", "m", "t", "w", "h", "f", "s"]
	return weekdays[int(time.strftime('%w'))]


def get_status(location_id):
	"""
	returns: list of hours for given location on current weekday
	"""
	try:
		location = locations[location_id]
	except KeyError:
		return None
	today = get_weekday()

	for i in location['hours']:
		if today in i:
			hours = []
			for time in location['hours'][i]:
				is_open = False
				if inside_time_range(time[0], time[1]):
					is_open = True
				location_dict = {
						'open': time[0],
						'close': time[1],
						'is_open': is_open
				}
				hours.append(location_dict)
			return {
					'name': location['name'],
					'hours': hours,
					'id': location_id,
					'is_open': is_open
					}


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
	today_hours = []
	for location in locations:
		hours = get_status(location)
		if hours is not None:
			today_hours.append(hours)
	return today_hours


if __name__ == 'miami_api':
	get_json_data()
