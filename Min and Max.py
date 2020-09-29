import numpy

if __name__ == "__main__":
    arr = []
    n, m = input().split()
    n = int(n)
    m = int(m)
    for _ in range(n):
        x = list(map(int, input().split()))
        x = x[:m]
        arr.append(x)
    min = numpy.min(arr, axis=1)
    print(numpy.max(min))
