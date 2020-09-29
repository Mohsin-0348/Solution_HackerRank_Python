import re

n = int(input())
for i in range(n):
    str = input()
    valid = ['7','8','9']
    match = re.search(r'\d'*10, str)

    if match and len(str) == 10:
        for item in valid:
            if str.startswith(item):
                print('YES')
                break
        else:
                print('NO')
    else:
        print('NO')
