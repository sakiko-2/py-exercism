from collections import Counter
import re

def count_words(sentence):
    return Counter(re.findall(r"\b[\w']+\b", sentence.replace("_", " ").lower()))
