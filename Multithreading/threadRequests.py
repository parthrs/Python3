#!/usr/bin/env python3

import requests
import time
import threading
import queue

def make_http_requests(server_address, input_q, output_q):
  """
  A worker function that runs perpetually to, pick a request object from the input queue,
   poll the http server in server.py, and write the result back to the output queue
  :server_address: (tuple) Input server address tuple of the form ('ip address', port)
    ::'ip address':: (string) can be 'localhost' if server.py is running on the same machine
    ::port:: (int) port at which server.py listens
  :input_q: (Queue) an input queue to pick request objects from
  :output_q: (Queue) an output queue to write the result of the request into
  """
  while True:
    request_n = input_q.get()
    resp = requests.get("http://{0}:{1}".format(server_address[0], server_address[1]))
    output_q.put((request_n, str(resp.text)))
    input_q.task_done()

if __name__ == "__main__":

  # Set total number of requests that will be made to the server
  num_requests = 14

  # Set number of threads/workers that will be spawned
  threads = 10

  # Set the server address same as server.py module
  server_address = ('localhost', 60998)

  # Declare input and output queues
  input_queue = queue.Queue()
  output_queue = queue.Queue()

  # Note the start time
  start_time = time.time()

  # Spawn Daemon threads
  for _i in range(threads):
    worker = threading.Thread(target=make_http_requests, args=(server_address, input_queue, output_queue), daemon=True)
    worker.start()

  # Inject requests into the input queue
  for _i in range(num_requests):
    input_queue.put(_i+1)

  # Wait for all worker threads to finish
  input_queue.join()
  print("Summary:")
  print("Took {0} seconds to make {1} requests".format(str(time.time() - start_time), num_requests+1))
  print("")
  print("Per request stats:")
  for _i in output_queue.queue:
    print("Request # {0} took {1} seconds for the server to process".format(*_i))
