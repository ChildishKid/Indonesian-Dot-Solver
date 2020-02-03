__all__ = {"dfs"}


def dfs(start: str, goal: str, max_depth: int = 10):
    from spaces import action_space
    search_log = []
    solution_log = []
    action_space = action_space(len(start))

    __dfs(action_space, start, goal, search_log, solution_log, max_depth=max_depth)

    if solution_log:
        solution_log.append(f'0 {start}')
        solution_log.reverse()
    else:
        solution_log = ['no solution']

    return search_log, solution_log


"""
action_space:
    A dict containing the string identifier of an action as a key followed by its equivalent list of indices represented actions.

    refer to 'indonesian_dot/spaces/action_space.py'

state_space:
    The starting string value of a node

    Example:
        '010111010'
goal_state:
    The ending string value of a node

    Example:
        '000000000'

max_depth:
    The maximum depth of the dfs algorithm set to 10 by default

solution_log:
    A list that dfs can use to append the solution
    
search_log:
    A list that dfs can use to append the search space

"""


def __dfs(action_space, state_space, goal_state, search_log, solution_log, max_depth=10):
    search_log.append(state_space)
    if state_space == goal_state:
        return True
    elif max_depth <= 0 or not action_space:
        return False

    int_start = int(state_space, 2)
    new_depth = max_depth - 1
    form = '0' + str(len(state_space)) + 'b'

    int_result = [(k, f'{v ^ int_start:{form}}') for k, v in action_space.items()]
    int_result = dict(sorted(int_result, key=lambda x: x[1]))
    copy_d = {}
    copy_d.update(action_space)

    for k, v in int_result.items():
        del copy_d[k]

        ans = __dfs(copy_d, v, goal_state, search_log, solution_log, max_depth=new_depth)
        if ans:
            solution_log.append(f'{k} {v}')
            return True

        search_log.append(state_space)
