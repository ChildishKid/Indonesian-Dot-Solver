from collections import OrderedDict

from spaces import DiGraph


def puzzle_metadata():
    return OrderedDict([
        ('state_current', None),
        ('state_final', None),
        ('size', None),
        ('observation_space', DiGraph),
        ('action_space', indonesian_action_builder),
    ])
