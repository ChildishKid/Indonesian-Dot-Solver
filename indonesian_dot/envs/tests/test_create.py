import numpy

from envs.indonesian_env import IndonesianEnv

state = [0, 1, 0,
         1, 1, 1,
         0, 1, 0]

state = numpy.array(state)
state = state.reshape((3, 3))

board = IndonesianEnv(state)

var = board.history_space
print(var)
