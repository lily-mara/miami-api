#!/usr/bin/env python3
import json
import time
import requests
from bs4 import BeautifulSoup
import re
import os

locations = None


def get_person_info(name):
	name = name.replace('_', '+')
	name = name.replace(' ', '+')

	options = {'query_type': 'simple',
		'query_operator': 'equals',
		'query_filter_type': 'people',
		'query_string': name,
		'run_query': 'Search'
	}
	url = 'http://community.miamioh.edu/phpapps/directory/'

	info_page = requests.get(url, params=options).text

	soup = BeautifulSoup(info_page)
	
	try:
		id_search = re.search('([a-zA-Z]*) at miamioh dot edu', info_page)
		id = id_search.group(1)
	except AttributeError:
		return {'error': 'No person found with that name'}

	email = id + '@miamioh.edu'

	info = {
			'name': soup('p', {'class': 'result_list_entry_name'})[0].string,
			'id': id,
			'email': email
	}
	
	return info


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
	file_path = os.path.join(os.path.dirname(__file__), 'locations.json')
	with open(file_path, 'r') as json_file:
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
			is_open = False
			for time_period in location['hours'][i]:
				this_time_is_open = False
				if inside_time_range(time_period[0], time_period[1]):
					this_time_is_open = True
					is_open = True
				location_dict = {
						'open': time_period[0],
						'close': time_period[1],
						'is_open': this_time_is_open
				}
				hours.append(location_dict)
			return {
					'name': location['name'],
					'hours': hours,
					'id': location_id,
					'is_open': is_open,
					'time': time.strftime('%H:%M')
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
