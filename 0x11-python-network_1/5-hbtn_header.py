#!/usr/bin/python3
'''A Python script that fetches a URL
& displays the value of the variable X-Request-Id in the response header'''

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # a response obj called r
    r = requests.get(url)

    # grab the value of X-Request-Id
    id = r.headers['X-Request-Id']
    print(id)
