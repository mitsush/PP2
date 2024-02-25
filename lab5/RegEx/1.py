# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.


import re

def main(s : str) -> str:
    subRE = r"ab*"

    if re.match(subRE, s):
        return "Match found"
    else:
        return "Not found"
    
with open('row.txt', 'r', encoding='utf8') as f:
    txt = f.read()

print(main(txt))
