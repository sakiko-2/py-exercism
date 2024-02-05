def steps(num):
    if num <= 0: raise ValueError("Only positive integers are allowed")

    result = 0

    while num > 1:
        num = num / 2 if num % 2 == 0 else 3 * num + 1

        result += 1
    
    return result
