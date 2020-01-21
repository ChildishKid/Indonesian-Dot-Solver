# Indonesian_Dot_Solver

## File Structure
```angular2html
Indonesian-Dot-Solver
├── src
|   ├── genericSolution.py
|   ├── agent.py
|   ├── environment.py
|   ├── space.py
├── res
├── test
├── COMP_472_2020_Winter_Project_1.pdf
├── README.md
```
```

src:
    Contains all python source code to solve the Indonesian puzzle.

    src/genericSolution.py:
        Contains a mathematical solution to the project's requirement.
        This must be removed before submission.

    src/agent.py:
        This file contains our implementation for DFS, BFS, and A* generic algorithms.
        Classes residing in an Agent will be used in Space.py
        Classes within Environment.py will use a parameter of generic type referencing the Agent.py

    src/environment.py:
        This file contains all implementations for the logic of the Indonesian Dot Puzzle board.
        Concerns relating to the board itself are handled here.

    src/space.py:
        This file resolves all interaction concerns between the program and the user's input when the game is started.
        Parsing, Resolution, and calls are made here.

        We may change this at a later time to be the __init__.py file


res:
    Contains all resources that are optional or mandatory for the project to run.


test:
    Contains all files used for testing the functionality of classes in the src folder.


COMP_472_2020_Winter_Project_1.pdf:
    The business requirements of the project
```




