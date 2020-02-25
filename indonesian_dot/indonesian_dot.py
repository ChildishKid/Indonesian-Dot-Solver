from argparse import ArgumentParser
from logging import info, getLogger, INFO
from multiprocessing.pool import Pool
from os import getcwd
from os.path import isfile
from time import time

import agents
from envs import Puzzle

"""

The main entry of the program.

The program is start from the directory of this file, and requires resources folder to be one level higher.

"""
DEFAULT_DIR = getcwd()
RESOURCES = DEFAULT_DIR[:DEFAULT_DIR.rfind('/')] + '/resources/'
DEFAULT_FILE = RESOURCES + 'test'
AGENTS = ['bfs', 'dfs', 'a*']
ARGS = ['size',
        'max_d',
        'max_l',
        'state'
        ]

parser = ArgumentParser(description='Solves the Indonesian Dot Puzzle')
parser.add_argument('-v', '--verbose', help='enable verbose logging.', action="store_true")
args = parser.parse_args()

if args.verbose:
    getLogger().setLevel(INFO)


# This function is responsible for printing general error messages
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

info(f"Reading the contents of '{DEFAULT_FILE}'")
try:
    for line in lines:
        if line == '\n':
            continue

        l_arr = line.split(' ')
        l_arr[-1] = l_arr[-1][:-1]
        l_arr[:-1] = [int(e) for e in l_arr[:-1]]

        assert len(l_arr) == len(ARGS)
        assert len(l_arr[-1]) == int(l_arr[0]) ** 2
        assert int(l_arr[-1], 2)
        assert all(int(x) >= 0 for x in l_arr[:-1])

        copy = {ARGS[i]: l_arr[i] for i in range(len(ARGS))}
        commands.append(copy)
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

responses = {}

puzzles = []
for command in commands:
    puzzle = Puzzle(command['state'])
    puzzle.max_depth = command['max_d']
    puzzle.max_length = command['max_l']
    puzzles.append(puzzle)


def run(agent):
    for puzzle in puzzles:
        start = time()
        solution, search = puzzle.traverse(agent)
        stop = time()
        print(
            f'\033[92m Indonesian Dot Puzzle #{puzzle.id} solved in {(stop - start) * 1000:.3} ms using {agent}.\033[0m')
        saving_file_path = f'{RESOURCES}{puzzle.id}_{agent}_'

        try:
            info(f"Saving Puzzle #{puzzle.id}\'s {agent} search data")
            f = open(saving_file_path + 'search', 'w')
            f.writelines(search)
            f.close()

            info(f"Saving Puzzle #{puzzle.id}\'s {agent} solution data")
            f = open(saving_file_path + 'solution', 'w')
            f.writelines(solution)
            f.close()
        except (FileNotFoundError, FileExistsError, IsADirectoryError):
            print(f"File path resulted in an error and was ignored.")


agents = [agents.make(x) for x in AGENTS]
p = Pool(len(agents))
p.map(run, agents)
# threads = [Thread(target=run, args=(x,)) for x in agents]
"""
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()"""
print('Done')
