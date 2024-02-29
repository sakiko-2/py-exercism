nums = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
romans = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")

def roman(number):
    result = ""

    for idx, num in enumerate(nums):
        while num <= number:
            result += romans[idx]
            number -= num

    return result
