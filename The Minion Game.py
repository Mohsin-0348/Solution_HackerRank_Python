def minion_game(string):
    vowels = ('A', 'E', 'I', 'O', 'U')
    kevin = 0
    stuart= 0
    for i in range(len(string)):
        if s[i] in vowels:
            kevin += (len(string)-i)
        else:
            stuart += (len(string)-i)
    
    if kevin > stuart:
        print("Kevin", kevin)
    elif kevin < stuart:
        print("Stuart", stuart)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
