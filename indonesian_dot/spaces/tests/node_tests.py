import unittest

from spaces.node import Node


class MyTestCase(unittest.TestCase):
    def test_something(self):
        first = Node('010111010', None, 0)
        second = Node('000000000', first, 4)

        print(first)
        print(second)
        print(second.search_artifact())
        print(second.solution_artifact())
        print(first.search_artifact())
        print(first.solution_artifact())

    def test_contains(self):
        state = '010111010'
        first = Node(state)
        assert state in first

    def test_le(self):
        first = Node('010111010')
        second = Node('000000000')

        assert second <= first

    def test_lt(self):
        first = Node('010111010')
        second = Node('000000000')

        assert second < first

    def test_cmp(self):
        first = Node('010111010')
        second = Node('000000000')

        assert -1 == second.__cmp__(first)


if __name__ == '__main__':
    unittest.main()
