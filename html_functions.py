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
		close_time = format_time(location[1][1])
		return_list.append({
			'name': location[0],
			'to_close' : to_close,
			'close_time': close_time
			})

	return return_list


def get_time_to_close(close):
	if type(close) == int:
		close = str(close)
	close += ' ' + str(time.strftime('%Y-%m-%d'))
	close_time = time.strptime(close, '%H%M %Y-%m-%d')

	close_epoch = time.mktime(close_time)
	now_epoch = time.time()

	difference = time.gmtime(close_epoch - now_epoch + 60)

	difference_string = time.strftime('%Hh:%Mm', difference)
	return difference_string


def format_time(to_format):
	in_time = time.strptime(str(to_format), '%H%M')
	return time.strftime('%I:%M %p', in_time)


if __name__ == '__main__':
	main()
