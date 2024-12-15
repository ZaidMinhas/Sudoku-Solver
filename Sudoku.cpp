#include "Sudoku.h"
#include <fstream>
#include <iostream>
using namespace std;


Sudoku::Sudoku(const string& filename) {
    //Read sudoku board from file, blanks = 0
    ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Error: Could not open the file." << std::endl;
    }

    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            int value;
            file >> value;
            board[i][j] = value;
            if (value == 0) {
                empty.push_back(i*9 + j);
            }
        }
    }
    file.close();
}

void Sudoku::display(const string& sym) const {
    cout << "\n";
    for (int r = 0; r < 9; r++) {
        if (r%3 == 0) {
            for (int p = 0; p < 13 ; p++){ std::cout << sym << " ";}
            std::cout << "\n";
        }
        for (int c = 0; c < 9; c++) {
            if (c%3 == 0) {
                std::cout << sym << " ";
            }
            if (board[r][c] == 0) {
                std::cout << "  ";
            }
            else {
                std::cout << board[r][c] << " ";
            }

        }
        std::cout << sym << "\n";
    }
    for (int p = 0; p < 13 ; p++){ std::cout << sym << " ";}
    std::cout << "\n";
}

void Sudoku::solve() {
    solve(0);
}

void Sudoku::reset(const int i) {
    int r = i/9;
    int c = i%9;
    board[r][c] = 0;
}


bool Sudoku::solve(const int i) {
    const int cell = empty[i];

    for (int count = 1; count < 10; count++) {
        if (test_and_set(cell, count)) {
            if ( i == empty.size()-1 || solve(i+1)) {
                return true;
            }
        }
    }
    reset(cell);
    return false;
}

bool Sudoku::test_and_set(const int i, const int val) {
    const int r = i / 9;
    const int c = i % 9;
    const int temp = board[r][c];
    board[r][c] = val;

    if (validate(r, c)) {
        return true;
    }
    else {
        board[r][c] = temp;
        return false;
    }
}


//Check if a cell is valid by cross-checking wil block, row and column
bool Sudoku::validate(const int r, const int c) const {
    return checkBlock(r, c) && checkRow(r,c) && checkColumn(r,c);
}

//Checks full block
bool Sudoku::checkBlock(const int r, const int c) const {
    const int b_row = 3*(r/3);
    const int b_col = 3*(c/3);
    const int value = board[r][c];

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {

            int curr_row = b_row + i;
            int curr_col = b_col + j;

            if (curr_row == r && curr_col == c) continue;
            if (board[curr_row][curr_col] == value) return false;
        }
    }

    return true;
}

//Checks full row
bool Sudoku::checkRow(const int r, const int c) const {
    const int value = board[r][c];
    for (int i = 0; i < 9; i++) {
        if (i == r) continue;
        if (board[i][c] == value) return false;
    }
    return true;
}

//Checks full column
bool Sudoku::checkColumn(const int r, const int c) const {
    const int value = board[r][c];
    for (int i = 0; i < 9; i++) {
        if (i == c) continue;
        if (board[r][i] == value) return false;
    }
    return true;
}