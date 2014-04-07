import json

times = None
with open('times.json', 'r') as json_file:
	times = json.load(json_file)

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
