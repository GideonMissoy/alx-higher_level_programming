#!/usr/bin/python3
"""
This module uses funtions save_to_json_file and load_from_json_file
This script adds all args to a python list, and then save to a file
"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = 'add_item.json'

try:
    json_list = load_from_json_file(file)
except FileNotFoundError:
    json_list = []

for arg in args_list:
    json_list.append(arg)

# Save the list to add_item.json
save_to_json_file(json_list, file)
