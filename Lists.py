
if __name__ == '__main__':

    li = []
    n = int(input())
    for _ in range(n):
        x = input().split()
        if x[0].lower() == 'insert':
            li.insert(int(x[1]), int(x[2]))
        elif x[0].lower() == 'append':
            li.append(int(x[1]))
        elif x[0].lower() == 'remove':
            li.remove(int(x[1]))
        elif x[0].lower() == 'pop':
            li = li[:-1]
        elif x[0].lower() == 'print':
            print(li)
        elif x[0].lower() == 'sort':
            li.sort()
        elif x[0].lower() == 'reverse':
            li.reverse()
    
