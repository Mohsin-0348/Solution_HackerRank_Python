import numpy

if __name__ == "__main__":
    a = []
    b = []
    count = 0
    numpy.set_printoptions(legacy='1.13')
    n = int(input())
    for _ in range(2*n):
        x = list(map(int, input().split()))
        if count < n:
            a += [x[:n]]
        else:
            b += [x[:n]]
        count += 1
    print(numpy.matmul(a, b))
