def convert(number):
    raindrops = { 3: "Pling", 5: "Plang", 7: "Plong" }
    result = ""

    for num, sound in raindrops.items():
        if number % num == 0:
            result += sound
    
    return result if result != "" else str(number)
