// 문제 : https://www.acmicpc.net/problem/1018

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int check(vector<string> grid, int y, int x) {
    int Bcount = 0;
    int Wcount = 0;

    for (int i=y; i<y+8; i++) {
        for (int j=x; j<x+8; j++) {
            int cy = i - y;
            int cx = j - x;
            if ((cy + cx) % 2 == 0) {
                if (grid[i][j] == 'B') {
                    Wcount ++;
                } else {
                    Bcount ++;
                }
            }
            if ((cy + cx) % 2 == 1) {
                if (grid[i][j] == 'B') {
                    Bcount ++;
                } else {
                    Wcount ++;
                }
            }
        }
    }
    return min(Wcount, Bcount);
}

int main() {
    int N, M;
    int MAX = 64;

    cin >> N >> M;
    cin.ignore(256,'\n');

    vector<string> grid; 
    for(int i=0; i<N; i++) {
        string tmp;
        getline(cin, tmp);
        grid.push_back(tmp);
    }
    for(int i=0; i<N-7; i++) {
        for(int j=0; j<M-7; j++) {
            int tmp = check(grid, i, j);
            if (MAX > tmp) { MAX = tmp; }
        }
    }
    cout << MAX << endl;
    return 0;
}