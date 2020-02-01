from collections import OrderedDict

"""
Configuration of vanilla data structure provision through builder functions.

These functions may be implemented outside of the Graph class, and the Graph classes will manipulate or react to 
the data within them
"""


def graph_metadata():
    return OrderedDict([
        ('node_struct', node_struct),
        ('node_attr', node_attr),
        ('edge_struct', edge_struct),
        ('edge_attr', edge_attr),
        ('max_depth', 50),
        ('is_directed', None),
        ('node_count', 0),
        ('edge_count', 0)
    ])


def node_struct():
    return OrderedDict()


def node_attr():
    return OrderedDict([
        ('degree', None),
        ('value', None),
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


def edge_struct():
    return OrderedDict()


def edge_attr():
    return OrderedDict([
        ('id', None),
        ('cost', None)
    ])
