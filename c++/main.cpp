#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int grid[9][9];
int answer = 0;
vector<pair<int, int>> zero;

void dfs(int index) {
    if (index == zero.size()) {
        answer++;
        return;
    }
    int y = zero[index].first;
    int x = zero[index].second;
    for (int i=0; i<10;i++) {
        bool flag = false;
        for (int a=0; a<9; a++) {
            if (grid[y][a] == i || grid[x][a] == i) {
                flag = true;
                break;
            }
            for (int yy = y/3;yy<y/3+3;yy++) {
                for (int xx = x/3;xx<x/3+3;xx++) {
                    if (grid[yy][xx] == i) {
                        flag = true;
                        break;
                    }
                }
            }
        }
        if (flag) continue;
        grid[y][x] = i;
        dfs(index + 1);
        grid[y][x] = 0;
    }
}

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
    
    for (int i=0; i<9; i++) {
        for (int j=0; j<9; j++) {
            cin >> grid[i][j];
            if (grid[i][j] == 0) {
                zero.push_back({i, j});
            }
        }
    }
    cout << answer << endl;
}