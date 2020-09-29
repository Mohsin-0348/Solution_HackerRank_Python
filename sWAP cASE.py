def swap_case(s):
    y = ''
    for letter in s:
        if letter.isupper():
            letter = letter.lower()
            y += letter
        elif letter.islower():
            letter = letter.upper()
            y += letter
        else:
            y += letter
    return y

