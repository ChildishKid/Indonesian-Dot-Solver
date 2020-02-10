from envs import Env


class Puzzle(Env):
    _action_space = None

    def __init__(self, actions, state):
        super().__init__(actions, state)

    def solved(self):
        return int(self._state, 2) == 0

    def sample(self):
        return self.state, self.actions

    def step(self, action):
        new_state = self._actions[action]
        i_st = int(new_state, 2)
        form = f'0{len(new_state)}b'
        act = [(k, f"{i_st ^ Puzzle._action_space[k]:{form}}")
               for k, v in self._actions.items()]

        act.sort(key=lambda x: x[1])
        act = dict(act)
        del act[action]
        return Puzzle(act, new_state), i_st == 0
