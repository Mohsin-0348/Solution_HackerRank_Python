def print_formatted(number):
    x = number
    width = len(bin(x)[2:])
    for i in range(1, x+1):
        print(str(i).rjust(width), oct(i)[2:].rjust(width), hex(i)[2:].upper().rjust(width), bin(i)[2:].rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
