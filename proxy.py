#!/usr/bin/env python
from webserver import Server, HTTPServer
from urlparse import urlparse
from sh import ct, echo
import urllib2

foreman_url = 'http://127.0.0.1:8080/unattended/provision'

class Proxy(Server):
    def do_GET(self):
        self._set_headers()
        myQuery = urlparse(self.path).query
        url = '{0}?{1}'.format(foreman_url, myQuery) if myQuery != '' else foreman_url
        yaml = str(urllib2.urlopen(url).read())
        print(yaml)
        ignition = str(ct(echo(yaml, _piped=True)))
        self.wfile.write(ignition)

def run(server_class=HTTPServer, handler_class=Proxy, port=80, content=None):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()