import agents
import envs

"""

The entry point of the Indonesian Puzzle Solver.

For the program to function properly, a path to a directory needs to be provided.
    Example: python3 indonesian_dot.py ../resources
    
Note: This path needs to contain a file with the name test.

The test file needs to contain 4 variables per line: 
    the dimension of the puzzle
    the maximum depth
    the maximum length
    the starting state of the puzzle

For any help, run the program with the help command:
    python3 indonesian_dot.py -h

"""


def run(arguments):
    from time import time
    agent = arguments[0]
    puzzle_list = arguments[1]
    resource = arguments[2]

    total = []
    for individual_puzzle in puzzle_list:
        start = time()
        solution, search = individual_puzzle.traverse(agent)
        stop = time()

        total.append(stop - start)
        saving_file_path = f'{resource}{individual_puzzle.id}_{agent}_'

        try:
            with open(saving_file_path + 'search.txt', 'w') as search_file:
                search_file.writelines(search)

            with open(saving_file_path + 'solution.txt', 'w') as solution_file:
                solution_file.writelines(solution)

        except (FileNotFoundError, FileExistsError, IsADirectoryError):
            print(f"File path resulted in an error and was ignored.")

    print(f'Agent {agent} average time is {(sum(total) / len(total)) * 1000:.3} ms.')


if __name__ == '__main__':
    from argparse import ArgumentParser
    from multiprocessing.pool import Pool
    from os.path import isfile, isdir, exists
    from os import listdir

    def internal_error(msg):
        parser.print_help()
        print()
        print(msg)
        exit(2)


    def puzzle_iterator():
        for agent in agent_list:
            yield [agent, puzzles, args.DIR]


    parser = ArgumentParser(description='Solves the Indonesian Dot Puzzle')
    parser.add_argument("DIR", help="Directory containing a file names test")

    args = parser.parse_args()

    if not exists(args.DIR):
        internal_error(f'{args.DIR} not an existing directory.')
    elif isfile(args.DIR):
        internal_error(f'{args.DIR} is not a directory.')

    directory_files = listdir(args.DIR)
    test_file = list(filter(lambda x: 'test' in x, directory_files))

    if len(test_file) > 1:
        internal_error('Multiple test files detected.')
    elif not test_file:
        internal_error('Test file not found.')
    args.DIR += '/' if '/' in args.DIR else '\\'
    test_file = args.DIR + test_file[0]

    if isdir(test_file):
        internal_error(f'{test_file} not a file.')

    puzzles = []
    agent_list = [agents.make(x) for x in ['dfs', 'bfs', 'astar']]

    lines = open(test_file).readlines()
    curr_line = 1

    try:
        for line in lines:
            if line == '\n':
                continue

            l_arr = line.split()
            max_d = int(l_arr[1])
            max_l = int(l_arr[2])
            state = l_arr[3]

            puzzle = envs.Puzzle(state, max_length=max_l, max_depth=max_d)
            puzzles.append(puzzle)

            curr_line += 1

    except (ValueError, TypeError):
        internal_error(f'Line #{curr_line} does not have appropriate attributes.')

    execution_plan = list(puzzle_iterator())

    pool = Pool(len(agent_list))
    pool.imap_unordered(run, execution_plan)
    pool.close()
    pool.join()
