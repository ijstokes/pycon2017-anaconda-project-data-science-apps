import sys

import tornado.web
import tornado.ioloop
import tornado.httpserver

from argparse import ArgumentParser

from tornado.options import define, options


class HostFilter(tornado.web.RequestHandler):
    def prepare(self):
        anaconda_project_hosts = self.application._application['anaconda_project_hosts']
        if self.request.host not in anaconda_project_hosts:
            print("{} not allowed in aborting...".format(self.request.host))
            print("Allowed hosts: {}".format(anaconda_project_hosts))
            raise tornado.web.HTTPError(403)


class QuoteHandler(HostFilter):
    def get(self, *args, **kwargs):
        quote = {'quote': "I've always been more interested in the future than in the past.",
                 'author': 'Grace Hopper'}
        self.write(quote)


class IndexHandler(HostFilter):
    def get(self, *args, **kwargs):
        prefix = self.reverse_url('quote')
        body = """
<html>
  <head>
    <title>Quote API Server</title>
  </head>
  <body>
    <p>This is a toy JSON API server example.</p>
    <p>Make a GET request to <a href="{prefix}">{prefix}</a></p>
  </body>
</html>
""".format(prefix=prefix)
        self.write(body)


class Application(tornado.web.Application):
    def __init__(self, anaconda_project_hosts):
        handlers = [
            tornado.web.url(r"/", IndexHandler),
            tornado.web.url(r"/quote", QuoteHandler, name="quote")
        ]
        tornado.web.Application.__init__(self, handlers, debug=True)
        self._application = dict(anaconda_project_hosts=anaconda_project_hosts)


if __name__ == "__main__":
    # arg parser for the standard project options
    parser = ArgumentParser(prog="quote-api", description="API server that returns a quote.")
    parser.add_argument('--anaconda-project-host', action='append',
                        help='Hostname to allow in requests')
    parser.add_argument('--anaconda-project-no-browser', action='store_true', default=False,
                        help='Disable opening in a browser')
    parser.add_argument('--anaconda-project-use-xheaders',
                        action='store_true',
                        default=False,
                        help='Trust X-headers from reverse proxy')
    parser.add_argument('--anaconda-project-url-prefix', action='store', default='',
                        help='Prefix in front of urls')
    parser.add_argument('--anaconda-project-port', action='store', default='8080',
                        help='Port to listen on')
    parser.add_argument('--anaconda-project-iframe-hosts',
                        action='append',
                        help=('Space-separated hosts which can embed us in an iframe'
                              ' per our Content-Security-Policy'))
    parser.add_argument('--anaconda-project-address',
                        action='store',
                        default='0.0.0.0',
                        help='IP address the application should listen on.')

    # This app accepts but ignores --anaconda-project-no-browser
    # because we never bother to open a browser, and accepts but
    # ignores --anaconda-project-iframe-hosts since iframing an API
    # makes no sense.

    args = parser.parse_args(sys.argv[1:])
    anaconda_project_hosts = args.anaconda_project_host
    anaconda_project_port = args.anaconda_project_port
    anaconda_project_address = args.anaconda_project_address

    if not anaconda_project_hosts:
        local_hosts = ['localhost', '127.0.0.1']
        anaconda_project_hosts = ['{}:{}'.format(host, anaconda_project_port)
                                  for host in local_hosts]

    define("port", default=anaconda_project_port, help="run on the given port", type=int)
    define("address", default=anaconda_project_address,
           help="IP address the application should listen on.", type=str)
    print("Tornado App running on {}:{} with accepted host: {}".format(
        anaconda_project_address,
        anaconda_project_port,
        anaconda_project_hosts))

    http_server = tornado.httpserver.HTTPServer(Application(anaconda_project_hosts))
    http_server.listen(options.port, address=options.address)
    tornado.ioloop.IOLoop.instance().start()
