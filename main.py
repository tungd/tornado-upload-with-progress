#!/usr/bin/env python
import logging
from tornado import web, options, ioloop


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render('dist/index.html')

@web.stream_request_body
class UploadHandler(web.RequestHandler):
    def initialize(self):
        self.bytes_read = 0

    def data_received(self, chunk):
        self.bytes_read += len(chunk)

    def post(self):
        for field_name, files in self.request.files.items():
            for info in files:
                filename, content_type = info["filename"], info["content_type"]
                body = info["body"]
                logging.info(
                    'POST "%s" "%s" %d bytes', filename, content_type, len(body)
                )

        self.write("OK")


if __name__ == '__main__':
    options.parse_command_line()

    routes = [
        (r'/upload', UploadHandler),
        (r'/', IndexHandler),
    ]

    settings = {
        'debug': True,
        'static_path': './dist'
    }

    web.Application(routes, **settings).listen(8888)
    ioloop.IOLoop.current().start()
