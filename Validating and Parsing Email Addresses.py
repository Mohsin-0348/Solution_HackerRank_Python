import email.utils
import re

n = int(input())
for i in range(n):
    
    x = input()
    name, mail = email.utils.parseaddr(x)

    regex = r'^[a-zA-Z][a-zA_Z0-9-._]+[@][a-zA-Z]+[.][a-zA-Z]{1,3}$'
    if re.search(regex, mail):
        print(x)
    
