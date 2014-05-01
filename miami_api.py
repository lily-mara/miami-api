#!/usr/bin/env python3
import json
import time
import requests
from bs4 import BeautifulSoup
import re
import os

locations = None


def get_classes(dept, number, campus='O'):
	url = 'http://www.admin.muohio.edu/cfapps/courselist/selection_display.cfm'

	payload = {
		'term': '201510',
		'campus': "	'O' ",
		'subj': dept,
		'course_type': '',
		'course': number,
		'crn': '',
		'title': '',
		'level': '',
		'begin_time': '',
		'end_time': '',
		'monday': 'M',
		'tuesday': 'T',
		'wednesday': 'W',
		'thursday': 'R',
		'friday': 'F',
		'saturday': 'S'
	}

	class_page = requests.post(url, data=payload).text
	soup = BeautifulSoup(class_page)

	class_soup = soup.findAll('tr', {'class' : re.compile('rowDetail_.*')})
	classes = []

	for class_section in class_soup:
		children = [i for i in class_section.children if i != '\n']

		has_class = lambda x, y: y in x['class']
		get_element = lambda x: str([i.string for i in children if has_class(i, x)][0])

		crn = get_element('colCrn')
		course = get_element('colCrse').replace('\u00A0', ' ')
		section = get_element('colSeq').replace(' ', '')
		title = get_element('colTitle')
		hours = get_element('colHrs')

		enrollment = get_element('colLim').split('/')
		enrolled = enrollment[0]
		max_students = enrollment[1]
		meet_times = get_element('colMeet').replace(' ', '')
		meet_days = get_element('colDays')
		room = get_element('colRoom')
		instructor = get_element('colInst')

		dates = get_element('colSpMeet')

		class_info = {
				'crn': crn,
				'course': course,
				'section': section,
				'title': title,
				'hours': hours,
				'enrolled': enrolled,
				'max_students': max_students,
				'meet_times': meet_times,
				'meet_days': meet_days,
				'room': room,
				'instructor': instructor,
				'dates': dates
		}

		classes.append(class_info)

	return classes


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
		id_search = re.search('([a-zA-Z0-9]*) at miamioh dot edu', info_page)
		id = id_search.group(1)
	except AttributeError:
		return {'error': 'No person found with that name', 'name': name}

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
