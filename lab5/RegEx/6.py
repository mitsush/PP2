# Write a Python program to replace all occurrences of space, comma, or dot with a colon.


import re

def main (s : str) -> str:
    symbols = [r'\s', r'\.', r',']

    for i in symbols:
        s = re.sub(i, ':', s)

    return s

with open('row.txt', 'r', encoding='utf8') as f:
    txt = f.read()

print(main(txt))
