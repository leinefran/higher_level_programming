#!/usr/bin/python3
# a Python script that fetches a URL

import urllib.request

if __name__ == "__main__":

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        t = type(html)
        output = html.decode(response.headers.get_content_charset())

        print("Body response:")
        print("\t- type: {}".format(t))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(output))
