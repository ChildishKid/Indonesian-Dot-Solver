from spaces import sample
from spaces.space import step

"""

dfs master function is fed a dictionary of arguments passed from agent_dict and extracts only variables it needs
such as the size, the depth, and the starting state.

this function then returns two lists: a search log, and a solution log

"""


def dfs(**kwargs):
    start = kwargs['start']
    max_depth = kwargs['max_depth']
    act_space = sample(kwargs['size'])

    search_log = []
    solution_log = []

    # a call is made to the private dfs method which uses recursion to solve the puzzle
    __dfs(act_space, start, search_log, solution_log, max_depth=max_depth)

    # if the solution log is not empty, then append the start state and the reverse the list
    if solution_log:
        solution_log.append(f'0 {start}')
        solution_log.reverse()

    # otherwise, the solution log contains an element no solution
    else:
        solution_log = ['no solution']

    return search_log, solution_log


"""

action_space:
    A dict containing the string identifier of an action as a key followed by its equivalent list of indices represented actions.

    refer to 'indonesian_dot/spaces/space.py'

state_space:
    The starting string value of a node

    Example:
        '010111010'

max_depth:
    The maximum depth of the dfs algorithm set to 10 by default

solution_log:
    A list that dfs can use to append the solution
    
search_log:
    A list that dfs can use to append the search space

"""


def __dfs(act_space, state_space, search_log, solution_log, max_depth=10):
    # whenever __dfs is called, a new node has been discovered. Append this node
    search_log.append(f'0 0 0 {state_space}')

    # If the integer value of the state is 0, then the puzzle is solved
    if int(state_space, 2) == 0:
        return True
    # Else if the max depth has been reached, backtrack
    elif max_depth <= 0 or not act_space:
        return False

    # The depth of the node is one level deeper, therefore we decrease the max_depth threshold
    new_depth = max_depth - 1

    # The results are computed by xor through the step function (see spaces/space)
    results = step(state_space, act_space)

    # The action space is copied
    copy_d = act_space.copy()

    """
    
    the key of the results and the key of the action_space are equivalent. 
    An action is expended every time a traversal is performed
    
    """
    for k, v in results.items():
        del copy_d[k]

        ans = __dfs(copy_d, v, search_log, solution_log, max_depth=new_depth)
        if ans:
            solution_log.append(f'{k} {v}')
            return True
