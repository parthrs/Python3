#!/usr/bin/env python3

import http.server
import time
import random
import threading

class RandomDelayHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.end_headers()
    rand_float = random.uniform(0.2,0.8)
    time.sleep(rand_float)
    self.wfile.write("Took {0} seconds".format(str(rand_float)).encode(encoding='utf_8'))

if __name__ == "__main__":

  httpd = http.server.ThreadingHTTPServer(('localhost', 60998), RandomDelayHTTPRequestHandler)
  #http_worker = threading.Thread(target=httpd.serve_forever, args=())
  #http_worker.setDaemon(True)
#  print("Server starting up")
  #http_worker.start()
#  print("Server started, sleeping for 10 secs..")
#  time.sleep(15)
  httpd.serve_forever()
