def score_words(words):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    score = 0
    for word in words:
        c = 0
        for letter in word.lower():
            if letter in vowels:
                c += 1
        if c % 2 == 0:
            score += 2
        else:
            score += 1
    return score



n = int(input())
words = input().split()
print(score_words(words))
