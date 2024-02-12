import re
import string

def is_pangram(sentence):
    txt = re.findall(r"[a-z]", sentence.lower())
    txt.sort()
    
    return set(txt) == set(list(string.ascii_lowercase))
