#!/usr/bin/python3
# a Python script that fetches a URL
# and displays the value of the X-Request-Id

import urllib.request, sys

if __name__ == "__main__":

    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.read()

        dic = response.info()
        id = dic.get('X-Request-Id')
        print(id)
