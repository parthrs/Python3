# An application of the python Multi-threading module

## This module demonstrates a use case for using multi-threading (as opposed to multi-processing) for I/O intensive operations.
## The server responding with a random delay tries to emulate a (rather slow)

1. server.py         - A simple http server that takes in requests (from threadRequests.py) and responds with a random delay 0.2 <= delay <= 0.8 seconds.
2. serialRequests.py - A client making requests to the http server on local host serially.
3. threadRequests.py - A simple client making requests to the server using multiple threads.

### E.g.
### Run the server.py in the background
#### python3.7 server.py &
