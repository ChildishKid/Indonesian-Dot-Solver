from agents.dfs import DFS
from spaces import DiGraph
import numpy
import argparse

#act as starting point for project
    #command line argument stuff
command_line_parser = argparse.ArgumentParser(description="Commandline arguments for program.")
command_line_parser.add_argument('--file_path', help='path to file to be read') # this will be unecessary (we use locals)
command_line_arguments = command_line_parser.parse_args()
"""
There is no need to use a graph object. Manpreet was using it on his DFS, you just call his DFS.

We removed graph class since we deemed it to be useless

Have a look at master's dfs algorithm. You will see it return a search and solution list

You to call it, then write the list returned to a file that is not in use.


"""
with open(command_line_arguments.file_path, "r") as file_read:#parse file
    if file_read != 'r':
        file_contents = file_read.readline()#assuming only one line to read
        file_line = file_contents.split(" ")#could instead overwrite file_contents variable
        puzzle_dimension = int(file_line[0])#converted to int for prepared_board
        max_depth = file_line[1]
        max_search_length = file_line[2]#currently not used
        board_state = file_line[3]
        #prepare variables for DFS.start(...)
        prepared_board = numpy.array(list(board_state)).reshape(puzzle_dimension, puzzle_dimension)
        closed_list = []
        open_list = []
        solution = []
        digraph_board = DiGraph()#name could be better
        digraph_board.add_node(0, move="0", value=prepared_board, depth=0)
        initial_node = digraph_board.node_at(0)
        DFS.start(initial_node, open_list, solution, closed_list, max_depth, digraph_board, 0)
        #output solution
        with open("dfs_solution.txt", "w") as file_write:
            for element in reversed(solution):
                file_write.write(' '.join(element))
                file_write.write('\n')
        file_write.close()
    else:
        print("Something went wrong, file not in read mode")
file_read.close()
