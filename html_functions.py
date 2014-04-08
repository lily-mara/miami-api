import miami_api
import time


def main():
	print(get_open_html())


def get_open_html():
	return_dict = {}
	open_dict = miami_api.get_open()
	open_list = list(open_dict.items())

	for location in open_list:
		time_string = get_time_to_close(location[1][1])
		return_dict.update({location[0]: time_string})

	return return_dict


def get_time_to_close(close):
	if type(close) == int:
		close = str(close)
	close += ' ' + str(time.strftime('%Y-%m-%d'))
	close_time = time.strptime(close, '%H%M %Y-%m-%d')

	close_epoch = time.mktime(close_time)
	now_epoch = time.time()

	difference = time.gmtime(close_epoch - now_epoch)

	difference_string = time.strftime('%Hh:%Mm', difference)
	return difference_string

if __name__ == '__main__':
	main()
