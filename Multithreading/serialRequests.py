#!/usr/bin/env python3

import requests
import time

def make_http_requests(server_address, request_n):
  """
  A simple function to poll the http server in server.py
  :server_address: (tuple) Input server address tuple of the form ('ip address', port)
    ::'ip address':: (string) can be 'localhost' if server.py is running on the same machine
    ::port:: (int) port at which server.py listens
  :request_n: (int) an identifier, allows tracking each request with number
  """
  resp = requests.get("http://{0}:{1}".format(server_address[0], server_address[1]))
  result_dict.append({request_n: "Status: {0}, Response: Server took {1}".format(resp.status_code, resp.text)})

if __name__ == "__main__":

  # Set total number of requests that will be made to the server
  num_requests = 14

  # Set the server address same as server.py module
  server_address = ('localhost', 60998)

  # Using a list to maintain order of request completion
  result_dict = []

  # Note start time
  start_time = time.time()

  # Making 20 requests serially
  for _i in range(num_requests):
    make_http_requests(server_address, _i+1)

  print("Took {0} seconds to make {1} requests".format(str(time.time() - start_time), num_requests+1))
  print(result_dict)
