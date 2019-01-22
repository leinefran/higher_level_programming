#!/usr/bin/python3
'''a Python script that takes in a string
& sends a search request to the Star Wars API'''

import requests
import sys

def main():
    url = 'https://swapi.co/api/people/?search='
    search = {'search': argv[1]}

    r = request.post(url, search)

    result = r.json()
    print("Number of results: {}".format(result))

if __name__ == "__main__":
