#!/bin/bash
# a Bash script that displays the size of the body of a URL response
curl -si "$1" | grep "Content-Length" | cut -d' ' -f2
