import numpy

from envs.indonesian_puzzle_env import IndonesianPuzzleEnv

state = [0, 1, 0,
         1, 1, 1,
         0, 1, 0]

state = numpy.array(state)
state = state.reshape((3, 3))

board = IndonesianPuzzleEnv(state)


var = board.action_space
action = var[4]
print("=============ACTION SPACE=============")
for x in var:
    print(x, '\n')
print("======================================")
var = board.observation_space
print("==========OBSERVATION SPACE===========")
print(var)
print("======================================")
board.step(action)
var = board.observation_space
print("========NEW OBSERVATION SPACE=========")
print(var)
print("======================================")
