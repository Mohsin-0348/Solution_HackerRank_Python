import re

def count_substring(string, sub_string):
    ln = len(sub_string)
    c = 0
    for i in range(len(string)):
        if re.search(sub_string, string[i:(i+ln)]):
            c += 1
    return c

