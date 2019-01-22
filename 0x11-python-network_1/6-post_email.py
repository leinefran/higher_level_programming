#!/usr/bin/python3
'''A Python script that fetches a URL
& displays the value of the variable X-Request-Id in the response header'''

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    r = requests.get(url, params=values)

    print(r.text)
