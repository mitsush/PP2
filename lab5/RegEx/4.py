# Write a Python program to find the sequences of one upper case letter followed by lower case letters.


import re

def main(s : str):

    subRE = r"[A-Z][a-z]+"

    if re.match(subRE, s):
        return "Match Found"
    else:
        return "Not Found"

with open('row.txt', 'r', encoding='utf8') as f:
    txt = f.read()
    
print(main(txt))
