import email.utils
import re

lines = []
n = int(input())
for i in range(n):
    lines.append(input())

regex = r'#[a-fA-F0-9]{3,6}'
for line in lines:
    if re.search(r':', line) and re.search(regex, line):
        colors = re.findall(regex, line)
        for color in colors:
            color_ln = len(color)
            if color_ln % 3 == 1 and color_ln < 8:
                print(color)
