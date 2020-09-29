import numpy

if __name__ == "__main__":
    arr = []
    numpy.set_printoptions(legacy='1.13')
    n = int(input())
    for _ in range(n):
        x = list(map(float, input().split()))
        arr += [x[:n]]
    print(round(numpy.linalg.det(arr), 2))
