import numpy

if __name__ == "__main__":
    x = list(map(float, input().split()))
    numpy.set_printoptions(sign=' ')
    my_arr = numpy.array(x)
    print(numpy.floor(my_arr))
    print(numpy.ceil(my_arr))
    print(numpy.rint(my_arr))
