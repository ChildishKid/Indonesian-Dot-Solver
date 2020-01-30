import numpy as np


# Winning condition: All 0's
def check_win(values):
    if type(values) is not np.ndarray:
        raise TypeError
    if '1' in values:
        return False
    else:
        return True


# Switch values between 0 and 1
def switch(value):
    if value == '0':
        return '1'
    else:
        return '0'


# Perform action move
def action(values, position):
    if type(values) is not np.ndarray and type(position) is not tuple:
        raise TypeError
    x, y = position
    x_max, y_max = values.shape
    new_values = np.copy(values)

    # Center
    new_values[x][y] = switch(new_values[x][y])

    # Up
    if x != 0:
        new_values[x - 1][y] = switch(new_values[x - 1][y])

    # Down
    if x != x_max - 1:
        new_values[x + 1][y] = switch(new_values[x + 1][y])

    # Left
    if y != 0:
        new_values[x][y - 1] = switch(new_values[x][y - 1])

    # Right
    if y != y_max - 1:
        new_values[x][y + 1] = switch(new_values[x][y + 1])

    # return np.copy(new_values)
    return new_values


# Rows represented by letters and columns by numbers - to display search/solution path and storing in closed
def convert_move(position):
    x, y = position
    return chr(65 + x).__str__() + y.__str__()


# Convert ndarray to string - to display search/solution path
def to_str(values):
    if type(values) is not np.ndarray:
        return TypeError
    return "".join(str(x) for x in values.flatten())
