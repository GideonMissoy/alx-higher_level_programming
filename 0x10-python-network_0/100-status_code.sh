#!/bin/bash
# Script sends a request to URL passed as arg and display the resp status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
