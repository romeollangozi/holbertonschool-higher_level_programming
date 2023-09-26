#!/usr/bin/python3
import hidden_4
array = dir(hidden_4)
if __name__ == "__main__":
    for definitions in array:
        if definitions[0] != '_':
            print(definitions)
