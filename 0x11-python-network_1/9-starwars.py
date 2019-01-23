#!/usr/bin/python3
'''a Python script that takes in a string
& sends a search request to the Star Wars API'''

import requests
import sys
if __name__ == "__main__":

    search = sys.argv[1]
    url = 'https://swapi.co/api/people/?search=' + search

    r = requests.get(url)

    result = r.json()

    print("Number of results: {}".format(result['count']))
    for name in result['results']:
        print(name['name'])
