from collections import OrderedDict
from spaces import DiGraph
from spaces import action_space


class Puzzle(object):
    size = None
    max_depth = None
    max_length = None
    action_space = None
    obs_space = DiGraph()

    def __init__(self, state, actions=None, depth=0, length=0):
        self.current_state = state
        self.current_actions = actions
        self.depth = depth
        self.length = length
        Puzzle.obs_space.put_node(self)

    def step(self, a: set):
        if self.depth > Puzzle.max_depth:
            raise RuntimeError(f'Maximum depth has been reached.')

        var = int(self.current_state, 2)
        new_depth = self.depth + 1
        new_length = 0
        new_puzzles = []

        for b in a:
            new_state = var ^ self.action_space[b]
            new_act = self.current_actions.difference({a})
            new_puzzles.append(Puzzle(new_state, new_act, new_depth, new_length))
            new_length += 1

        # sort the puzzle according to the __le__ method
        return new_puzzles.sort()






        new_state = int(self.current_state, 2)
        new_state = self.action_space[a] ^ new_state
        is_solved = new_state == 0
        str_format = '0' + str(Puzzle.size) + 'b'
        new_state = f'{new_state:{str_format}}'

        new_act =

        new_depth = self.depth + 1

        new_puzzle = Puzzle(new_state, new_act, new_depth, )
        self.obs_space.put_node(new_state, depth=new_depth, action=new_act)
        self.obs_space.put_edge((self, new_state), id=a)

        return self.current_memory, is_solved

    def __eq__(self, other):
        return self.current_state == other.current_state

    def __ne__(self, other):
        return self.current_state != other.current_state

    def __hash__(self):
        return self.current_state

    def __gt__(self, other):
        return self.current_state > other.current_state

    def __lt__(self, other):
        return self.current_state < other.current_state

    def __le__(self, other):
        return self.current_state <= other.current_state

    def __ge__(self, other):
        return self.current_state >= other.current_state

    @staticmethod
    def make(size: int, max_depth: int, max_length: int, state: str):
        del Puzzle.action_space
        Puzzle.obs_space.reset()

        Puzzle.size = size ** 2
        Puzzle.max_depth = max_depth
        Puzzle.max_length = max_length
        Puzzle.action_space = action_space(size)
        return Puzzle(state)
