#!/usr/bin/env python3

"""Type-annotated function concat"""

def concat(str1: str, str2: str) -> str:
    """Returns a concatenated string"""
    return f"{str1}{str2}"

str1 = "egg"
str2 = "shell"

print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)
