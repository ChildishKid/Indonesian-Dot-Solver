import numpy

from envs.indonesian_board import IndonesianBoard

state = [0, 1, 0,
         1, 1, 1,
         0, 1, 0]

state = numpy.array(state)
state = state.reshape((3, 3))

board = IndonesianBoard(state)

var = board.history_space
print(var)
