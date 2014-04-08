#!/usr/bin/env python3
import tornado.autoreload
import tornado.ioloop
import tornado.web
import json
import subprocess

import miami_api

class OpenLocationHandler(tornado.web.RequestHandler):
	def get(self):
		response = miami_api.get_open()
		json_response = json.dumps(response, indent=4 * ' ')
		self.set_header('Content-Type', 'application/json')
		self.write(json_response)

class HoursHandler(tornado.web.RequestHandler):
	def get(self, location):
		response = miami_api.get_hours(location)
		json_response = json.dumps(response, indent=4 * ' ')
		self.set_header('Content-Type', 'application/json')
		self.write(json_response)

class TodayHoursHandler(tornado.web.RequestHandler):
	def get(self):
		response = miami_api.get_today_hours()
		json_response = json.dumps(response, indent=4 * ' ')
		self.set_header('Content-Type', 'application/json')
		self.write(json_response)

class GithubHookHandler(tornado.web.RequestHandler):
	def post(self):
		subprocess.call(['git', 'pull', 'origin', 'master'])
		self.write('Update completed sucessfully')

	def get(self):
		self.write('update?')

application = tornado.web.Application([
	(r'/miami/open', OpenLocationHandler),
	(r'/miami/hours/([a-zA-Z_]+)', HoursHandler),
	(r'/miami/today', TodayHoursHandler),
	(r'/miami/update', GithubHookHandler),
	(r'/favicon\.ico',tornado.web.StaticFileHandler, {'path': './images/favicon.ico'},)
])

if __name__ == '__main__':
	application.listen(5000)
	tornado.autoreload.watch('miami_server.py')

	ioloop = tornado.ioloop.IOLoop.instance()
	tornado.autoreload.start(ioloop)
	ioloop.start()
