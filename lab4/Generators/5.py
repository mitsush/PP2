# Implement a generator that returns all numbers from (n) down to 0.


def reverse_order(n):
    for i in range(n + 1, 0, -1):
        yield i - 1

numbers = reverse_order(50)

print(list(numbers))
