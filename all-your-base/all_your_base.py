def rebase(input_base, digits, output_base):
    if input_base < 2: raise ValueError("input base must be >= 2")

    for d in digits:
        if d < 0 or d >= input_base: raise ValueError("all digits must satisfy 0 <= d < input base")

    if output_base < 2: raise ValueError("output base must be >= 2")
    
    if not digits or not sum(digits): return [0]

    number = sum([n * input_base ** idx for idx, n in enumerate(digits[::-1])])

    result = []

    while number > 0:
        result.insert(0, number % output_base)
        number //= output_base

    return result
