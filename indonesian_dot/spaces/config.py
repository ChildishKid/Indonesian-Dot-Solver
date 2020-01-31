from collections import OrderedDict

"""
Configuration of vanilla data structure provision through builder functions.

These functions may be implemented outside of the Graph class, and the Graph classes will manipulate or react to 
the data within them
"""


def graph_metadata():
    return OrderedDict([
        ('max_depth', 50),
        ('is_directed', None),
        ('node_count', 0),
        ('edge_count', 0),
        ('node_struct', node()),
        ('node_attr', node_attr),
        ('node_pred', None),
        ('node_suc', None),
        ('edge_struct', edge()),
        ('edge_attr', edge_attr)
    ])


def node():
    return OrderedDict()


def node_attr():
    return OrderedDict([
        ('degree', None),
        ('depth', None),
    ])


def node_pred():
    return OrderedDict()


def node_pred_builder():
    return OrderedDict()


def node_suc():
    return OrderedDict()


def node_suc_builder():
    return OrderedDict()


def edge():
    return OrderedDict()


def edge_attr():
    return OrderedDict([
        ('action', None),
        ('weight', None)
    ])
