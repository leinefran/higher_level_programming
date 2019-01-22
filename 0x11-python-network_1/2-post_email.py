#!/usr/bin/python3
'''a Python script that fetches a URL
and displays the value of the X-Request-Id'''

import urllib.request
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        the_page = response.read()

    print(the_page)
