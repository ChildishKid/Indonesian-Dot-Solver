from .agent import Agent
from .astar_agent import AStarAgent
from .bfs_agent import BFSAgent
from .dfs_agent import DFSAgent

__all__ = {'Agent', 'AStarAgent', 'DFSAgent', 'BFSAgent', 'make'}


def make(agent_type):
    if agent_type == 'dfs':
        return DFSAgent()
    elif agent_type == 'bfs':
        return BFSAgent()
    elif agent_type == 'astar':
        return AStarAgent()
