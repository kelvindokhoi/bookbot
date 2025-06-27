from collections import Counter

def word_count(text):
    return len(text.split())

def count_characters(text):
    f_text = dict(Counter(text.lower()))
    return f_text

def sorted_chars(d:dict):
    return sorted([{k:v} for k,v in d.items()],key=lambda x:list(x.values())[0],reverse=True)