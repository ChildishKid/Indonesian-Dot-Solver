from argparse import ArgumentParser
from multiprocessing.pool import Pool
from os import getcwd
from os.path import isfile
from time import time

import agents
from envs import Puzzle

DEFAULT_DIR = getcwd()
RESOURCES = DEFAULT_DIR[:DEFAULT_DIR.rfind('/')] + '/resources/'
DEFAULT_FILE = RESOURCES + 'test'

puzzles = []
agent_list = ['dfs', 'bfs', 'astar']


def internal_error(msg):
    print(f'\033[91m {msg} \033[0m')
    exit(-1)


def convert_puzzle():
    lines = open(DEFAULT_FILE).readlines()
    curr_line = 1

    try:
        for line in lines:
            if line == '\n':
                continue

            l_arr = line.split(' ')
            l_arr[-1] = l_arr[-1][:-1]
            l_arr[:-1] = [int(e) for e in l_arr[:-1]]

            assert len(l_arr) == 4
            assert len(l_arr[-1]) == int(l_arr[0]) ** 2
            assert int(l_arr[-1], 2)
            assert all(int(x) >= 0 for x in l_arr[:-1])

            max_d = l_arr[1]
            max_l = l_arr[2]
            state = l_arr[3]

            puzzle = Puzzle(state, max_length=max_l, max_depth=max_d)
            puzzles.append(puzzle)

            curr_line += 1

    except (ValueError, AssertionError, TypeError):
        internal_error(f'Line #{curr_line} does not have appropriate attributes.')


def run(agent):
    total = []
    for puzzle in puzzles:
        start = time()
        solution, search = puzzle.traverse(agent)
        stop = time()

        total.append(stop - start)
        saving_file_path = f'{RESOURCES}{puzzle.id}_{agent}_'

        try:
            with open(saving_file_path + 'search.txt', 'w') as search_file:
                search_file.writelines(search)

            with open(saving_file_path + 'solution.txt', 'w') as solution_file:
                solution_file.writelines(solution)

        except (FileNotFoundError, FileExistsError, IsADirectoryError):
            print(f"File path resulted in an error and was ignored.")

    print(f'\033[92m Agent {agent} average time is {(sum(total) / len(total)) * 1000:.3} ms.\033[0m')


if __name__ == '__main__':
    parser = ArgumentParser(description='Solves the Indonesian Dot Puzzle')
    args = parser.parse_args()

    if 'indonesian_dot' not in DEFAULT_DIR:
        internal_error('indonesian_dot.py must be run inside of "indonesian_dot" folder.')

    if not isfile(DEFAULT_FILE):
        internal_error(f'File {DEFAULT_FILE} not found.')

    convert_puzzle()
    agent_list = [agents.make(x) for x in agent_list]
    process_pool = Pool(len(agent_list))
    process_pool.map(run, agent_list)
    process_pool.close()
    process_pool.join()
    print('Done')
