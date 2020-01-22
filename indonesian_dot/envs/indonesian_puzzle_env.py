from indonesian_dot.spaces.action_space import ActionSpace
from spaces.observation_space import ObservationSpace
from spaces.space import Space
from .env import Env

"""
An environment for simulating the Indonesian Puzzle using matrix manipulations
"""


class IndonesianPuzzleEnv(Env):

    def __init__(self, **kwargs):
        super().__init__()

        if 'observation' in kwargs:
            state = kwargs.get('observation')
            assert isinstance(state, Space)

            self._observation_space = state

        else:
            self._observation_space = ObservationSpace()

        if 'action' in kwargs:
            state = kwargs.get('action')
            assert isinstance(state, Space)

            self._action_space = state

        else:
            self._action_space = ActionSpace()

        self._history_space = []
        self.__max_depth = self._observation_space.__len__()

    """
    The environment will only accept new actions if these actions do not exceed the maximum depth value set
    when either the environment has been first solved. The maximum depth value decreases as new solutions are found
    and are better than the previous solutions.
    """

    def step(self, action):
        stop_flag = len(self._history_space) >= self.__max_depth
        if stop_flag:
            return self._observation_space.sample(), \
                   self._history_space, \
                   [False, stop_flag]

        response = self._action_space.step(action)
        solved = not self._observation_space.contains(0)

        if response:
            self._history_space.append(action)
            self._observation_space.step(action)

            if solved:
                self.__max_depth = len(self._history_space)

        return self._observation_space.sample(), \
               self._history_space, \
               [solved, not stop_flag]

    def revert(self):
        if self._history_space:
            action = self._history_space.pop()
            self._observation_space.revert(action)
            self._action_space.revert(action)

    def reset(self):
        while self._history_space:
            self.revert()
