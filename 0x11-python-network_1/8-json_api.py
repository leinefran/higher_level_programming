#!/usr/bin/python3
'''Python script that takes in a letter
& sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter'''


import requests
import sys
if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) > 1:
        letter = {'q': sys.argv[1]}
    r = requests.post(url, letter)

    try:
        info = r.json()
        if info:
            id = info.get("id")
            name = info.get("name")
            print("[{}] {}".format(id, name))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
