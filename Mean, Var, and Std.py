import numpy

if __name__ == "__main__":
    arr = []
    numpy.set_printoptions(sign=' ')
    n, m = input().split()
    n = int(n)
    m = int(m)
    for _ in range(n):
        x = list(map(int, input().split()))
        x = x[:m]
        arr.append(x)
    print(numpy.mean(arr, axis=1))
    print(numpy.var(arr, axis=0))
    print(format(numpy.std(arr), '.11f'))
