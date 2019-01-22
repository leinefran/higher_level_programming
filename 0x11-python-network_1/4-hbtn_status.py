#!/usr/bin/python3
'''A Python script that fetches a URL'''

import requests

if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    t = type(r)

    print("Body response:")
    print("\t- type: {}".format(t.text))
    print("\t- content: {}".format(r.text))
