#!/usr/bin/env python3
import tornado.escape
import tornado.ioloop
import tornado.web

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

application = tornado.web.Application([
	(r'/miami/open', OpenLocationHandler),
	(r'/miami/hours/([a-zA-Z]+)', HoursHandler),
	(r'/miami/today', TodayHoursHandler)
])

if __name__ == '__main__':
	application.listen(5000)
	tornado.ioloop.IOLoop.instance().start()
