if __name__ == "__main__":
    x, y = input().split()
    x, y = int(x), int(y)
    sep = '-'
    inc = 1
    if x*3 == y:
        for i in range(x):
            if i < x//2:
                print(('.|.'*inc).center(y, sep))
                inc += 2
            elif i == x//2:
                print('WELCOME'.center(y, sep))
            else:
                inc -= 2
                print(('.|.'*inc).center(y, sep))
