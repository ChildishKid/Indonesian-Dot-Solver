from spaces import action_space


def bfs(**kwargs):
    size = kwargs['size']
    start = kwargs['start']
    max_length = kwargs['max_length']
    act_space = action_space(size)

    search_log = []
    solution_log = []
    queue = [start]

    actions = {start: list(act_space.keys())}
    lengths = {start: 0}
    predecessors = {}

    form = '0' + str(len(start)) + 'b'

    while queue:
        curr_state = queue.pop(0)

        next_length = lengths[curr_state] + 1

        if next_length >= max_length:
            continue

        state_action = actions[curr_state]

        for i in range(len(state_action)):
            next_state = f'{act_space[state_action[i]] ^ int(curr_state, 2):{form}}'
            search_log.append(f'0 0 {next_state}')
            try:
                actions[next_state] = state_action[i+1:]
                queue.append(next_state)
            except IndexError:
                pass

            predecessors[next_state] = (state_action[i], curr_state)
            lengths[next_state] = next_length

            if int(next_state, 2) == 0:
                queue.clear()
                break

        queue.sort()


    i = ['0'] * len(start)
    i = "".join(i)

    while i != start:
        action, prev_state = predecessors[i]
        solution_log.append(f'{action} {i}')
        i = prev_state

    solution_log.append(f'0 {i}')
    solution_log.reverse()
    return search_log, solution_log


