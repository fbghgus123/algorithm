// 문제 : https://www.acmicpc.net/problem/3197

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>

using namespace std;

char grid[1500][1500];
bool visited[1500][1500];

int r, c;
vector<pair<int, int>> swan;

vector<pair<int, int>> waterQ;
vector<pair<int, int>> waterNextQ;
vector<pair<int, int>> swanQ;
vector<pair<int, int>> swanNextQ;

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

bool bfs(pair<int, int> start) {
    queue<pair<int, int>> q;
    q.push(start);
    visited[start.first][start.second] = true;
    while (q.size() > 0) {
        pair<int, int> tmp = q.front();
        q.pop();

        int y = tmp.first;
        int x = tmp.second;
        for (int i=0; i<4; i++) {
            int cy = y + dy[i];
            int cx = x + dx[i];
            if (0 <= cy && 0 <= cx && cy < r && cx < c) {
                if (cy == swan[1].first && cx == swan[1].second) return true;
                if (visited[cy][cx] == false ) {
                    visited[cy][cx] = true;
                    if (grid[cy][cx] == '.') q.push({cy, cx});
                    if (grid[cy][cx] == 'X') swanNextQ.push_back({cy, cx});
                }
            }
        }
    }
    return false;
}

void melt() {
    for (int i=0; i<waterQ.size(); i++) {
        pair<int, int> tmp = waterQ[i];
        int y = tmp.first;
        int x = tmp.second;

        for (int j=0; j<4; j++) {
            int cy = y + dy[j];
            int cx = x + dx[j];
            if (grid[cy][cx] == 'X') {
                grid[cy][cx] = '.';
                waterNextQ.push_back({cy, cx});
            }
        }
    }
}

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> r >> c;
    for (int i=0; i<r; i++) {
        for (int j=0; j<c; j++) {
            cin >> grid[i][j];
            if (grid[i][j] == 'L') swan.push_back({i, j});
            if (grid[i][j] != 'X') waterQ.push_back({i, j});
        }
    }

    bool flag = false;
    int count = 0;
    swanQ.push_back(swan[0]);
    while (flag == false) {
        for (int i=0; i<swanQ.size(); i++) {
            flag = bfs(swanQ[i]);
            if (flag) {
                cout << count << endl;
                break;
            }
        }
        if (flag) break;
        
        melt();
        waterQ = waterNextQ;
        waterNextQ.clear();

        swanQ = swanNextQ;
        swanNextQ.clear();
        count ++;
    }
}