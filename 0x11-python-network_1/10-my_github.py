#!/usr/bin/python3
'''a Python script that takes your Github credentials
& uses the Github API to display your id'''

import requests
import sys
if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]

    r = requests.get('https://api.github.com/user',
                     auth=(username, password))

    try:
        print(r.json().pop('id'))
    except:
        print("None")
