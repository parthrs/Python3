# An application of the python Multi-threading module

### This module demonstrates a use case for using multi-threading (as opposed to a serial/single threaded approach) for I/O intensive operations.
### The server responds to a http get request with a random delay, emulating a (rather slow) http server that takes finite amount of to respond -
### - often the case dealing with web applications.

1. server.py         - A simple http server that takes in requests (from threadRequests.py) and responds with a random delay 0.2 <= delay <= 0.8 seconds.
2. serialRequests.py - A client making requests to the http server on local host serially.
3. threadRequests.py - A simple client making requests to the server using multiple threads.

### E.g.
### Run the server.py in the background
#### python3.7 server.py &
### Run the requests program
#### python3.7 threadRequests.py

### Sample output for threadRequests.py with 10 threads and 15 requests
Summary:
Took 1.6501476764678955 seconds to make 15 requests

Request # 2 took Took 0.24867925249657535 seconds seconds for the server to process
Request # 4 took Took 0.38333063910986476 seconds seconds for the server to process
Request # 8 took Took 0.5032725998549821 seconds seconds for the server to process
Request # 11 took Took 0.2850061247068584 seconds seconds for the server to process
Request # 6 took Took 0.5493392002715208 seconds seconds for the server to process
Request # 7 took Took 0.7278569953772984 seconds seconds for the server to process
Request # 3 took Took 0.7442683673333161 seconds seconds for the server to process
Request # 12 took Took 0.5152251648799313 seconds seconds for the server to process
Request # 13 took Took 0.5267893472839107 seconds seconds for the server to process
Request # 14 took Took 0.6213304370643036 seconds seconds for the server to process
Request # 10 took Took 0.36988110314060674 seconds seconds for the server to process
Request # 5 took Took 0.4376267981603784 seconds seconds for the server to process
Request # 1 took Took 0.46904684851395934 seconds seconds for the server to process
Request # 9 took Took 0.6085180059444326 seconds seconds for the server to process
