# Write a function that accepts string from user and print all permutations of that string.

def print_permutations(s, prefix=""):
    if len(s) == 0:
        print(prefix)
    else:
        for i in range(len(s)):
            rem = s[:i] + s[i+1:]
            print_permutations(rem, prefix + s[i])

user_input = input()
print_permutations(user_input)