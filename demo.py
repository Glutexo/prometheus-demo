from os import getenv
from prometheus_client import start_http_server, Summary
from random import random
from time import sleep


listen_port = getenv('LISTEN_PORT', 8080)

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary("request_processing_seconds", "Time spent processing request")


# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """
    A dummy function that takes some time.
    """
    sleep(t)


if __name__ == "__main__":
    # Start up the server to expose the metrics.
    start_http_server(listen_port)
    # Generate some requests.
    while True:
        process_request(random())
