# Write a Python program to find sequences of lowercase letters joined with a underscore.


import re

def main(s : str):
    subRE = r"[a-z]+_[a-z]+"

    if re.match(subRE, s):
        return "Match Found"
    else:
        return "Not Found"
    
with open('row.txt', 'r', encoding='utf8') as f:
    txt = f.read()

print(main(txt))

