#!/usr/bin/python3
'''a Python script that takes in a string
& sends a search request to the Star Wars API'''

import requests
import sys
if __name__ == "__main__":

    url = 'https://swapi.co/api/people/?search='
    search = {'search': sys.argv[1]}

    r = requests.get(url, search)

    result = r.json()

    print("Number of results: {}".format(result['count']))
    for name in result['results']:
        print(name['name'])
