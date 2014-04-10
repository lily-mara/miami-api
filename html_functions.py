import time

import miami_api


def main():
	print(get_open_for_html())


def get_open_for_html():
	"""
	Returns list of dicts holding information to be used by the dynamic
	'index.html' page upon loading. Each dict in the list is formatted as
	follows:

	{
		'name': name of dining location,
		'to_close': time remaining until close formatted like '03h:12m'
		'close_time': time of close formatted like '11:00 PM',
		'style': the HTML style tag to use for these cells
	}

	"""
	return_list = []
	open_dict = miami_api.get_open()
	open_list = list(open_dict.items())

	for location in open_list:
		to_close = get_time_to_close(location[1][1])
		to_close_string = get_close_string(to_close)
		close_time = format_time(location[1][1])
		style = get_style(to_close)

		return_list.append({
			'name': location[0],
			'to_close': to_close_string,
			'close_time': close_time,
			'style': style
		})

	return return_list


def get_style(time_to_close):
	"""
	Takes the remaining open time for a location and returns an HTML style
	string to be used on the row in the page. Currently, this only
	includes background color.
	"""

	if time_to_close < 60 * 60:
		# Red for times less than one hour
		return 'background:#cc9999'
	if time_to_close < 60 * 60 * 2:
		# yellow for times less than two hours
		return 'background:#ffcc99'
	# green otherwise
	return 'background:#99cc99'


def get_close_string(time_to_close):
	"""
	Given a time in seconds, this will format it as a string like 03h:12m
	"""
	time_to_close = time.gmtime(time_to_close)
	close_string = time.strftime('%Hh:%Mm', time_to_close)
	return close_string


def get_time_to_close(close):
	"""
	Returns the difference (in seconds) between the given parameter,
	'close', and the current time.
	"""
	if type(close) == int:
		close = str(close)
	close += ' ' + str(time.strftime('%Y-%m-%d'))
	close_time = time.strptime(close, '%H%M %Y-%m-%d')

	close_epoch = time.mktime(close_time)
	now_epoch = time.time()

	difference = close_epoch - now_epoch + 60
	return difference


def format_time(to_format):
	"""
	Takes a string in the format 2200 and returns a string in the format
	11:00 PM
	"""
	in_time = time.strptime(str(to_format), '%H%M')
	return time.strftime('%I:%M %p', in_time)


if __name__ == '__main__':
	main()
