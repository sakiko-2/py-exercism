def primes(limit):
    numbers = range(2, limit + 1)
    marked = [m for n in numbers for m in range(n * 2, limit + 1, n)]

    return [n for n in numbers if n not in marked]
