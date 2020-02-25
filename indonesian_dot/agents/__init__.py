from .agent import Agent
from .dfs_agent import DFSAgent
from .bfs_agent import BFSAgent
from .a_star_agent import AStarAgent

__all__ = {'Agent', 'AStarAgent', 'DFSAgent', 'BFSAgent', 'make'}


def make(agent_type):
    if agent_type == 'dfs':
        return DFSAgent()
    elif agent_type == 'bfs':
        return BFSAgent()
    elif agent_type == 'a*':
        return AStarAgent()
