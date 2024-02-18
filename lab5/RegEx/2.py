# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.


import re

def main(s : str) -> str:
    subRE = r"ab{2,3}"

    if re.match(subRE, s):
        return "Match found"
    else:
        return "Not Found"
    
with open('row.txt', 'r', encoding='utf8') as f:
    txt = f.read()

print(main(txt))
