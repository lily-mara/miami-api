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

class UpdateHandler(tornado.web.RequestHandler):
	def post(self):
		subprocess.call(['git', 'pull', 'origin', 'master'])
		self.write('Update completed sucessfully')

application = tornado.web.Application([
	(r'/miami/open', OpenLocationHandler),
	(r'/miami/hours/([a-zA-Z]+)', HoursHandler),
	(r'/miami/today', TodayHoursHandler),
	(r'/miami/update', UpdateHandler)
])

if __name__ == '__main__':
	application.listen(5000)
	tornado.autoreload.watch('miami_server.py')

	ioloop = tornado.ioloop.IOLoop.instance()
	tornado.autoreload.start(ioloop)
	ioloop.start()
