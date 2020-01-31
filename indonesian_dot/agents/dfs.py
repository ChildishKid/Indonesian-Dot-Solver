from utils import helper
import numpy as np


# For Sample Test
# from spaces import DiGraph

class DFS:
    @staticmethod
    def start(current_node, search, solution, closed, max_depth, graph, index):
        values = current_node["value"]
        depth = current_node["depth"]
        move = current_node["move"]

        # Check to see if winning pattern is found
        if helper.check_win(values):
            solution.append((move, helper.to_str(values)))
            return "Pass"

        # Check to see if max depth is reached
        elif depth == max_depth:
            return "Failed"

        # Otherwise, go further down
        else:
            depth += 1

            # Add failed move to closed list
            closed.append((move, np.array_str(values)))

            x_max, y_max = values.shape

            # Loop through each child
            for x in range(x_max):
                for y in range(y_max):
                    new_move = helper.convert_move((x, y))
                    new_value = helper.action(values, (x, y))
                    new_index = index * (y_max + 1) * (x_max + 1) + x + y + 1
                    graph.add_node(new_index, move=new_move, value=new_value, depth=depth)
                    graph.add_edge((index, new_index))  # Not used for included for sake of completion
                    new_node = graph.__getattr__(new_index)

                    # Append to search since we visit it
                    search.append((0, 0, 0, new_value))

                    # Verify if move has already been done (i.e. exist within closed)
                    if (new_move, np.array_str(values)) in closed:
                        continue

                    returned = DFS.start(new_node, search, solution, closed, max_depth, graph, new_index)

                    if returned != "Failed":
                        solution.append((move, helper.to_str(values)))
                        return "Pass"

        if depth == 0:
            return "No Solution"
        else:
            return "Failed"


"""
== SAMPLE TEST ===
z = "111001011"
Z = "1111111111111111"
# w = np.array(list(z)).reshape(3, 3)
w = np.array(list(Z)).reshape(4, 4)
close = []
open = []
solution = []
graph = DiGraph()
graph.add_node(0, move="0", value=w, depth=0)
initial_node = graph.__getattr__(0)
DFS.start(initial_node, open, solution, close, 9, graph, 0)
print(solution)
"""
