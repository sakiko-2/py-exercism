import re

def count_words(sentence):
    result = {}

    for word in re.findall(r"\b[\w']+\b", sentence.replace("_", " ").lower()):
        if result.get(word, "not found") == "not found":
            result[word] = 1
        else:
            result[word] += 1

    return result
