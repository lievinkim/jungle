
import sys

input_value = input()

if type(input_value) == int:
    print(chr(input_value))
else:
    print(ord(input_value))