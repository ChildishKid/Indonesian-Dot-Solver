from os import getcwd
from os.path import isfile
from time import time

from agents.config import agent_dict
from agents.dfs import dfs

"""

The main entry of the program.

The program is start from the directory of this file, and requires resources folder to be one level higher.

"""
DEFAULT_DIR = getcwd()
DEFAULT_PATH = DEFAULT_DIR[:DEFAULT_DIR.rfind('/')] + '/resources/'
DEFAULT_FILE = DEFAULT_PATH + 'test'
FUNCTION = [dfs]


# This function is response for printing general error messages
def internal_error(msg):
    print(f'\033[91m {msg} \033[0m')
    exit(-1)


if 'indonesian_dot' not in DEFAULT_DIR:
    internal_error('indonesian_dot.py must be run inside of "indonesian_dot" folder.')

if not isfile(DEFAULT_FILE):
    internal_error(f'File {DEFAULT_FILE} not found.')

"""

Start parsing the file and store it into commands.

All the lines of '../resources/test' are read, then stored into $lines. 

Each line must have it's size attribute be equivalent to the length of the state attribute

Each line must have the first three attributes represented as an integer and must be greater than or equal to 0

Each line must have it's last attribute represented as a string with only 0s and 1s


"""
commands = []
lines = open(DEFAULT_FILE).readlines()
curr_line = 1

try:
    for line in lines:
        if line == '\n':
            continue

        l_arr = line.split(' ')
        l_arr[-1] = l_arr[-1][:-1]
        l_arr[:-1] = [int(e) for e in l_arr[:-1]]

        c = agent_dict()
        key = list(c.keys())

        assert len(l_arr) == len(key)
        assert len(l_arr[-1]) == int(l_arr[0]) ** 2
        assert int(l_arr[-1], 2)
        assert all(int(x) >= 0 for x in l_arr[:-1])
        assert int(l_arr[-1], 2)

        c.update({key[i]: l_arr[i] for i in range(len(l_arr))})
        commands.append(c)
        curr_line += 1

except (ValueError, AssertionError, TypeError):
    internal_error(f'Line #{curr_line} does not have appropriate attributes.')

del lines
del curr_line

"""

The program has determined all commands are proper.

It will then run each agent in $FUNCTION against the commands

The output is stored in '../resources/_<#>_<name($FUNCTION)>_<search|solution>'

"""

for j in range(len(FUNCTION)):
    start = time()
    for i in range(0, len(commands)):
        func = FUNCTION[j]
        search, sol = func(**commands[i])

        search = [str(s) + '\n' for s in search]
        sol = [str(s) + '\n' for s in sol]
        reg = DEFAULT_PATH + str(i + 1) + '_' + func.__name__ + '_'

        f = open(reg + 'search', 'w')
        f.writelines(search)
        f.close()

        f = open(reg + 'solution', 'w')
        f.writelines(sol)
        f.close()
    stop = time()
    print(
        f'\033[92m Indonesian Dot Puzzle solved {len(commands)} puzzles in {(stop - start) * 1000:.3} ms using {FUNCTION[j].__name__}. \033[0m')
