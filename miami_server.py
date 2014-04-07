#!/usr/bin/env python3
import tornado.autoreload
import tornado.ioloop
import tornado.web
import subprocess

import miami_api

class OpenLocationHandler(tornado.web.RequestHandler):
	def get(self):
		response = miami_api.get_open()
		self.write(response)

class HoursHandler(tornado.web.RequestHandler):
	def get(self, location):
		response = miami_api.get_hours(location)
		self.write(response)

class TodayHoursHandler(tornado.web.RequestHandler):
	def get(self):
		response = miami_api.get_today_hours()
		self.write(response)

GitHub_POST_IPs = (
	'207.97.227.253',
	'50.57.128.197',
	'127.0.0.1'
)

class GithubHookHandler(tornado.web.RequestHandler):
	def post(self):
		if self.request.remote_ip not in GitHub_POST_IPs:
			self.send_error(status_code=403)
			return

		subprocess.call(['git', 'pull', 'origin', 'master'])
		print('updating')
		self.write('Update completed sucessfully')

	def get(self):
		self.write('update?')

application = tornado.web.Application([
	(r'/miami/open', OpenLocationHandler),
	(r'/miami/hours/([a-zA-Z]+)', HoursHandler),
	(r'/miami/today', TodayHoursHandler),
	(r'/miami/update', GithubHookHandler)
])

if __name__ == '__main__':
	application.listen(5000)
	tornado.autoreload.watch('miami_server.py')

	ioloop = tornado.ioloop.IOLoop.instance()
	tornado.autoreload.start(ioloop)
	ioloop.start()
