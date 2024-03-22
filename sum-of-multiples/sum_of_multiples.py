def sum_of_multiples(level, item_values):
    result = set()

    for v in item_values:
        result |= set(range(v, level, v)) if v > 0 else set([0])

    return sum(result)
