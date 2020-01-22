class Env(object):
    action_space = None
    observation_space = None
    history_space = None

    def step(self, action):
        raise NotImplementedError

    def revert(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError
