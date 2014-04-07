#!/usr/bin/env python3

from tornado.wsgi import WSGIContainer, WSGIApplication
from tornado.ioloop import IOLoop
from tornado.web import FallbackHandler, RequestHandler, Application
from tornado.httpserver import HTTPServer
from miami_server import app

miami_app = WSGIContainer(app)

if __name__ == "__main__":
	http_server = HTTPServer(miami_app)
	http_server.listen(5000)
	IOLoop.instance().start()
