from spaces import action_space


class stub(object):
    __states = None
    __action_space = None
    __format = None

    def __init__(self, state, size):
        self.current_state = state
        self.next_actions = None
        self.reset(state, size)

    def sample(self):
        if self.current_state in stub.__states:
            self.next_actions = stub.__states[self.current_state]
            # I dont want dfs to know what the results of the next actions are.
            return self.current_state, list(self.next_actions.keys())

        # convert the string state into an integer
        new_state = int(self.current_state, 2)
        # a new dictionary buffer to keep new values
        action_dict = {}
        for k, v in stub.__action_space:
            # xor it with the integer value of the action provided (i.e 'A1'), and convert to string
            value = f'{v ^ new_state:{format}}'
            # add the key of the action (i.e 'A1') and the value of the new state to action_dict
            action_dict[k] = value

        # now we have all actions, and new states. But, we want the new states with the leftmost zeros
        action_dict = sorted(action_dict, key=lambda x: x[1])

        # Let's save this as a dictionary
        self.next_actions = stub.__states[self.current_state] = dict(action_dict)

        # we don't want to show the new states to the DFS since it's a sample of actions
        return self.current_state, list(self.next_actions.keys())

    def step(self, action):
        # Dfs gave us an action and we now should commit this action

        if action not in self.next_actions:
            raise ValueError

        self.current_state = self.next_actions[action]
        return self.sample()

    def reset(self, state, size):
        del stub.__states
        del stub.__action_space

        stub.__action_space = action_space(size)
        stub.__format = '0' + str(len(self.current_state)) + 'b'
        stub.__states = {}
