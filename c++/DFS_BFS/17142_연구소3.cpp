// 문제 : https://www.acmicpc.net/problem/17142

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>

using namespace std;

int grid[50][50];
int visited[50][50];
int snapshot[50][50];
int N, M;
int answer = 2501;
vector<pair<int ,int>> virus;
vector<pair<int, int>> activate;

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

void bfs(pair<int, int> start) {
    queue<pair<int, int>> q;
    q.push(start);
    visited[start.first][start.second] = 0;
    while(q.size() != 0) {
        pair<int, int> current = q.front();
        q.pop();
        
        int y = current.first;
        int x = current.second;
        for (int i=0; i<4; i++) {
            int cy = y + dy[i];
            int cx = x + dx[i];
            if (0 <= cy && 0 <= cx && cy < N && cx < N) {
                if (grid[cy][cx] != 1 && (visited[cy][cx] > visited[y][x] + 1 || visited[cy][cx] == 0)) {
                    q.push({cy, cx});
                    visited[cy][cx] = visited[y][x] + 1;
                }
            }
        }
        
    }
}

int check() {
    int maxx = 0;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            if (grid[i][j] == 0 && visited[i][j] == 0) {
                return -1;
            }
            if (maxx < visited[i][j] && grid[i][j] != 2) maxx = visited[i][j];
        }
    }
    return maxx;
}

void btk(int start) {
    if (activate.size() == M) {
        int time = check();
        if (answer > time && time != -1) {
            answer = time;
            copy(&visited[0][0], &visited[0][0] + 2500, &snapshot[0][0]);
        }
        return ;
    }
    char tmp[50][50];
    for (int i=start; i<virus.size(); i++) {
        copy(&visited[0][0], &visited[0][0] + 2500, &tmp[0][0]);
        activate.push_back(virus[i]);
        bfs(virus[i]);
        btk(i+1);
        activate.pop_back();
        copy(&tmp[0][0], &tmp[0][0] + 2500, &visited[0][0]);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> N >> M;

    memset(visited, 0, sizeof(visited));

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> grid[i][j];
            if (grid[i][j] == 2) {
                virus.push_back({i, j});
            };
        }
    }
    btk(0);
    if (answer == 2501) answer = -1;
    cout << answer << endl;
}