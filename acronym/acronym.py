import re

def abbreviate(words):
    return "".join(re.findall(r"\b\w", re.sub(r"[^A-Z\s-]", "", words.upper())))
