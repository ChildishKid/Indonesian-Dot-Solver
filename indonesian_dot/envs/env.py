class Env:
    def __init__(self, actions, state):
        self._state = state
        self._actions = actions

    @property
    def state(self):
        return self._state

    @property
    def actions(self) -> list:
        return list(self._actions.keys())

    def solved(self) -> bool:
        raise NotImplementedError

    def sample(self):
        raise NotImplementedError

    def step(self, action):
        raise NotImplementedError

    @classmethod
    def make(cls, k, **kwargs):
        state = kwargs['state']
        size = kwargs['size']
        if k == 'puzzle':
            t_size = size ** 2
            actions = {}

            for i in range(t_size):
                val = sum([2 ** (t_size - 1 - x) for x in
                           [i - size,
                            i - 1 if i % size > 0 else -1,
                            i,
                            i + 1 if i % size < size - 1 else -1,
                            i + size]
                           if 0 <= x < t_size])
                key = chr(int(i / size) + 65) + str((i % size) + 1)
                actions[key] = val

            act = [(k, f"{int(state, 2) ^ v:{f'0{len(state)}b'}}") for k, v in actions.items()]
            act.sort(key=lambda x: x[1])
            act = dict(act)
            from envs.puzzle import Puzzle
            return Puzzle(act, state, actions)

        return None
