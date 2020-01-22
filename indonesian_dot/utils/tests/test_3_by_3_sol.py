# warning, will not work if the matrix is singular.
# the equation is not as accurate as you think it is because of rounding
import numpy

from utils.generic_algorithm import solve

example = numpy.array([0, 0, 1,
                       0, 1, 0,
                       1, 0, 0])
print(solve(example))
