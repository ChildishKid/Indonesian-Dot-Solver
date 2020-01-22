
class Env(object):
    """
    action_space: The list of actions that an agent can support
    observation_space: The state of the environment
    history_space: The list of previous actions performed on the board
    """
    def __init__(self):
        self._action_space = None
        self._observation_space = None
        self._history_space = None

    """
    Logic for stepping through a time-frame after executing an action
    
    Affects:
        observation_space
        action_space
        history_space
        
    Returns:
        observation_space : the new observation space after action is performed
        history_space : the new history space after action is performed
        info : a list of information
    """
    def step(self, action):
        raise NotImplementedError

    """
    Logic for reverting to the previous time-frame
    
    Affects:
        observation_space
        action_space
        history_space
    """
    def revert(self):
        raise NotImplementedError

    """
    Logic for resetting the entire state of the environment.
    
    Affects:
        observation_space
        action_space
        history_space 
    """
    def reset(self):
        raise NotImplementedError
