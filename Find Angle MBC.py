import math

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = math.sqrt(a**2 + b**2)
    angle = math.degrees(math.acos((b/c)))
    print(round(angle), u"\N{DEGREE SIGN}", sep='')
