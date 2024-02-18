# Create a generator that generates the squares of numbers up to some number N.


def squares_generator(N):
    i = 0
    while i <= N:
        yield i * i
        i += 1

generator = squares_generator(12)

print(list(generator))
        