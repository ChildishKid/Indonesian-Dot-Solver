from numpy import array, sqrt, zeros, identity, dot

"""
Example:

state = array([
        1, 1, 0, 1, 0, 0,
        1, 1, 0, 1, 1, 1,
        0, 0, 1, 1, 0, 0,
        1, 1, 1, 0, 1, 1,
        0, 1, 0, 0, 0, 0,
        1, 1, 0, 0, 0, 1
    ])
size = int(sqrt(len(state)))
solved_puzzle = solve_puzzle(state)
solved_puzzle = solved_puzzle.reshape((size, size))
print(solved_puzzle)
"""


def touch(target, action):
    length = len(target)
    row, column = divmod(action, length)

    if row - 1 >= 0:
        target[row - 1, column] += 1
    if row + 1 < length:
        target[row + 1, column] += 1
    if column - 1 >= 0:
        target[row, column - 1] += 1
    if column + 1 < length:
        target[row, column + 1] += 1
    target[row, column] = +1
    target %= 2


def action_creator(length):
    size = length ** 2
    actions = []
    for i in range(size):
        action = zeros((length, length), dtype=int)
        touch(action, i)
        action = action.reshape(size)
        actions.append(action)
    return array(actions)


def gauss_jordan_elimination(matrix):
    length = len(matrix)
    echelon_form = matrix.copy()
    inverse = identity(length, dtype=int)

    for i in range(length):

        for x in range(i, length):
            if echelon_form[x, i] == 1:
                echelon_form[[x, i]] = echelon_form[[i, x]]
                inverse[[x, i]] = inverse[[i, x]]
                break

        for j in range(length):
            if i == j or echelon_form[i, i] == 0:
                continue

            factor = echelon_form[j, i] / echelon_form[i, i]

            factor = int(factor)
            echelon_form[j, :] -= factor * echelon_form[i, :]
            inverse[j, :] -= factor * inverse[i, :]
            echelon_form[j, :] %= 2
            inverse[j, :] %= 2

    return inverse, echelon_form


def solve_puzzle(problem):
    length = int(sqrt(len(problem)))
    actions = action_creator(length)
    inverse_matrix, _ = gauss_jordan_elimination(actions)
    results = dot(inverse_matrix, problem)
    results %= 2
    return results
