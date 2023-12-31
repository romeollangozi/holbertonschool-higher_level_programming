#!/usr/bin/python3
'''
Module for demostrative purposes
'''


from sys import argv
from os.path import exists
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


my_list = []
if exists("add_item.json"):
    my_list = load_from_json_file("add_item.json")
for args in argv[1:]:
    my_list.append(args)
save_to_json_file(my_list, "add_item.json")
