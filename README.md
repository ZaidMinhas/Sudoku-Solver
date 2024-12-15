# C++ Implementation of a Sudoku Solver
I built a simple brute-force algorithm that solves any sudoku game

## How to run
Create a text file with a Sudoku board (fill empty squares with 0s, check Medium.txt for reference
Run the program and enter file path and name

## How it works
Program initalizes a vector of empty board positions
```cpp
if (cell_value == 0) {
  empty.push_back(pos);
}
```

Then solves the board recursivly
```cpp
Solve(index){
  cell = empty[index];
  for count -> [1,9]{
    if test_and_set(cell, count) && (i == empty.size()-1 || Solve(i+1))
      return true;
  }
  reset(cell);
  return false;
}
```

`test_and_set` checks if a cell value is valid by cross-checking with a cell block, row and column. If it is then it sets the value in the board. 
`reset` sets a cell back to 0, then backtracks to the previous cell
