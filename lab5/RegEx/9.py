# Write a Python program to insert spaces between words starting with capital letters.


import re

def main(s : str) -> str:
    listOfStrings = re.findall("[A-Z][^A-Z]*", s)
    answer = f"{listOfStrings[0]}"
    for i in listOfStrings[1::]:
        answer += ' ' + i

    return answer

with open('row.txt', 'r', encoding='utf8') as f:
    txt = f.read()

print(main(txt))
