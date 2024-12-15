#ifndef SUDOKU_H
#define SUDOKU_H
#include <iostream>
#include <vector>

using namespace std;

class Sudoku {
    int board[9][9]{};
    vector<int> empty;
    public:
    Sudoku();
    explicit Sudoku(const string& filename);
    ~Sudoku() = default;

    void display(const string& sym = "#") const;
    void solve();
    bool solve(int i);

    bool test_and_set(int i, int val);
    void reset(int i);
    bool validate(int r, int c) const;
    bool checkBlock(int r, int c) const;
    bool checkRow(int r, int c) const;
    bool checkColumn(int r, int c) const;



};

#endif //SUDOKU_H
