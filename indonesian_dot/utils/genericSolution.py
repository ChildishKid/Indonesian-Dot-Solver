import numpy
import math


def solve(init_matrix):

    size = init_matrix.shape[0]
    side = int(math.sqrt(size))
    b = numpy.ones(size)
    b = numpy.subtract(b, init_matrix)
    a = []

    for i in range(size):
        temp = numpy.zeros(size, int)
        temp[i] = 1

        if i - side >= 0:
            temp[i - side] = 1
        if i + side < size:
            temp[i + side] = 1
        if i % side != 0:
            temp[i - 1] = 1
        if i % side != side - 1:
            temp[i + 1] = 1

        a.append(temp)

    a = numpy.array(a)
    x = numpy.linalg.lstsq(a, b, None)[0]
    x = x.round()
    x = x % 2
    return x.reshape((side, side))
