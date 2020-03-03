# Indonesian Dot Puzzle Solver

The Indonesian Dot Puzzle is played on a n x n board. On each position of the board, a wooden token is placed.
Each token has 2 sides: one with a white dot (w), and the other with a black dot (b). Initially, the tokens are
placed on the board on a random side, and the goal is to find the smallest number of moves to bring the board
to its goal configuration, where all tokens have their white side up (w).

## Getting Started

It is suggested to read the [requirements](documentation/Requirements.pdf) and the [documentation](documentation/472_Project1_Report_26975852_40058821_26592006.pdf) pdf files prior to running the Indonesian Dot Puzzle Solver.


## Prerequisites

- Python 3.7+
- Numpy (optional for gauss/jordan strategy of solving)

## Usage

1. Clone the repository:
    ```shell script
    git clone git@github.com:Ra-Ni/Indonesian-Dot-Solver.git
    ```
    
2. Move into the [indonesian_dot](indonesian_dot) directory:
    
   ```shell script
   cd indonesian_dot
    ```

3. Run the python entry point with a path parameter pointing to the directory containing the test file:
    ```shell script
   python3 indonesian_dot.py <PATH>
    ```

## Configuration Files

1. Move into [resources](resources):
    ```shell script
    cd resources
    ```
2. Modify the [test](resources/test) file:
    ```shell script
    vim test
    ```
   or
   ```shell script
    nano test
    ```
   
3. Ensure that each line respects the following schema:
    ```shell script
    <dimension> <maximum depth> <maximum length> <state>
   
   dimension: the dimension of the board
   maximum depth: the maximum search depth of the search algorithm (doesn\'t affect bfs and a*)
   maximum length: the maximum length of the search path
   state: the initial state of the game
    ```

## Command Line Arguments

```shell script
indonesian_dot [OPTIONS] PATH
PATH:
    the path of the directory containing one test file.

OPTIONS: 
    -h, --help              prints the help menu

```

## Features

* Multi-processing support for the 3 search algorithms (DFS, BFS, A*)
* Fast convergence time*
* Polynomial time [solver](indonesian_dot/utils/poly_solve.py) 
* Combinatorial inspired algorithm to reduce redundancy during search

*: Depending on the size of the puzzle/configuration file.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Contributors

* [Rani Rafid](https://github.com/Ra-Ni) - 26975852
* [Gabriel Harris](https://github.com/Gabriel-T-Harris) - 40058821
* [Manpreet Tahim](https://github.com/ChildishKid) - 26592006

## Acknowledgement

* [PurpleBooth](https://github.com/PurpleBooth)'s template on README


[![GitHub Logo](assets/Octocat.png)](https://github.com/Ra-Ni/Indonesian-Dot-Solver)
