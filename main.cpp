#include <iostream>
#include "Sudoku.h"

int main() {
    //Read File
    string fileName;
    cout << "Please enter the file name: ";
    cin >> fileName;

    //Initialize board
    Sudoku sudoku(fileName);
    sudoku.display(".");

    //Solve game
    sudoku.solve();
    sudoku.display(".");

    //Keep program idle
    cin >> fileName;
    return 0;
}
