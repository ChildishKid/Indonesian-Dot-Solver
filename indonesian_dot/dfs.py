import helper
import node
import numpy as np


class DFS:
    @staticmethod
    def start(current_node, move, closed, depth, max_depth):
        values = current_node.get_values()

        # Check to see if winning pattern is found
        if helper.check_win(values):
            return move + " " + helper.to_str(values)

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

                    # Verify if move has already been done (i.e. exist within closed)
                    if (new_move, np.array_str(values)) in closed:
                        continue

                    new_value = helper.action(values, (x, y))
                    new_node = node.Node(current_node, new_value)

                    returned = DFS.start(new_node, new_move, closed, depth, max_depth)

                    if returned != "Failed":
                        return move + " " + helper.to_str(values) + "\n" + returned

        if depth == 0:
            return "No Solution"
        else:
            return "Failed"


z = "111001011"

w = np.array(list(z)).reshape(3, 3)
close = []
initial_node = node.Node(None, w)
print(DFS.start(initial_node, "A0", close, 0, 9))
