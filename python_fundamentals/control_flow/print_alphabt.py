#!/usr/bin/env python3
result = ""

for i in range(97, 123):
    if i == 101 or i == 113:
        continue

    new_char = chr(i)
    result = result + new_char

print("{}".format(result), end="")
