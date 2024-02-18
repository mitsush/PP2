# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.


def even_num_generator(n = int(input())):
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i 
        i += 1

even_numbers = even_num_generator()

for i in even_numbers:
    print(i, end=", ")
