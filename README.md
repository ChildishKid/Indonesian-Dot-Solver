# Indonesian Dot

## File/Folder Structure
```angular2html
.
├── indonesian_dot (root here)
|   ├── agents
|   ├── envs
|   ├── spaces
|   ├── utils
|   ├── tests
|   ├── core.py
├── .gitignore
├── COMP_472_2020_Winter_Project_1.pdf
├── README.md
```
```

indonesian_dot:
    The main python package for solving the puzzle

    indonesian_dot/utils:
        Any misc. python files or other files that are not required during the final submission

    indonesian_dot/agents:
        Our implementation for DFS, BFS, and A* generic algorithms.
        
    indonesian_dot/envs:
        All implementations for the logic of the Indonesian Dot Puzzle board.

    indonesian_dot/spaces:
        Resolves all interaction concerns between the program and the user's input when the game is started.
        Parsing, Resolution, and calls are made here.

    indonesian_dot/core.py:
        All abstract classes: ["Agent","Env","Space"] here.

    indonesian_dot/tests:
        Test folder for only core applications. For other tests, refer to the folder 'tests' in the specific package.


```




