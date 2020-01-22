import numpy

"""
Creates a list of actions that the IndonesianEnv supports. The elements found within the list are the shapes that are
supported for each element of the board
"""


def make(dimension=3):
    buffer = []
    size = dimension**2

    for i in range(size):
        temp = numpy.zeros(size, int)
        temp[i] = 1

        if i - dimension >= 0:
            temp[i - dimension] = 1
        if i + dimension < size:
            temp[i + dimension] = 1
        if i % dimension != 0:
            temp[i - 1] = 1
        if i % dimension != dimension - 1:
            temp[i + 1] = 1

        buffer.append(temp.reshape((dimension, dimension)))

    return buffer
