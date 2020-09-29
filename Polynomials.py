import numpy

if __name__ == "__main__":
    
    a = list(map(float, input().split()))
    b = int(input())
    print(numpy.polyval(a, b))
