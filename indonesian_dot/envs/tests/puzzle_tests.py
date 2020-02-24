import unittest

from numpy import array

from envs.puzzle import Puzzle


class MyTestCase(unittest.TestCase):

    def test_left_xor(self):
        p = Puzzle('000000000')
        for i in range(9):
            print(p.root_state)
            root = p.root_state
            n_c = p.step(root, i)
            lst = n_c.state_list()
            lst = array(lst).reshape((3, 3))
            print(lst)


if __name__ == '__main__':
    unittest.main()
