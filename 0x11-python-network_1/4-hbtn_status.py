#!/usr/bin/python3
'''A Python script that fetches a URL'''

import requests

if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    t = type(r.text)

    print("Body response:\n\t- type: {}\n\t-content: {}".format(
        t, r.text))
