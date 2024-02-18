# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.


def divisible_by_3_and_4(n):
    i = 0
    while i <= n:
        if(i % 3 == 0 and i % 4 == 0):
            yield i

        i += 1

numbers = divisible_by_3_and_4(100)

print(list(numbers))
