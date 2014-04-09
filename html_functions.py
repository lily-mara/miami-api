import miami_api
import time


def main():
	print(get_open_html())


def get_open_html():
	return_list = []
	open_dict = miami_api.get_open()
	open_list = list(open_dict.items())

	for location in open_list:
		to_close = get_time_to_close(location[1][1])
		to_close_string = get_close_string(to_close)
		close_time = format_time(location[1][1])
		color = get_color(to_close)

		return_list.append({
			'name': location[0],
			'to_close' : to_close_string,
			'close_time': close_time,
			'color': color
			})

	return return_list


def get_color(time_to_close):
	if time_to_close < 60 * 60:
		return 'background:#cc9999'
	if time_to_close < 60 * 60 * 2:
		return 'background:#ffcc99'
	return ''

def rgb_to_hex(rgb):
	return '#%02x%02x%02x' % rgb


def get_close_string(time_to_close):
	time_to_close = time.gmtime(time_to_close)
	close_string = time.strftime('%Hh:%Mm', time_to_close)
	return close_string


def get_time_to_close(close):
	if type(close) == int:
		close = str(close)
	close += ' ' + str(time.strftime('%Y-%m-%d'))
	close_time = time.strptime(close, '%H%M %Y-%m-%d')

	close_epoch = time.mktime(close_time)
	now_epoch = time.time()

	difference = close_epoch - now_epoch + 60
	return difference


def format_time(to_format):
	in_time = time.strptime(str(to_format), '%H%M')
	return time.strftime('%I:%M %p', in_time)


if __name__ == '__main__':
	main()
