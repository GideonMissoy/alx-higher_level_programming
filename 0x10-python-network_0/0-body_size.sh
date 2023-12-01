#!/bin/bash
# Script takes in URL, sends request to URL and displays size of body of resp
curl -s "$1" | wc -c
