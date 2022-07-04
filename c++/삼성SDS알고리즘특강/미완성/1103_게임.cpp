#include <iostream>
#include <algorithm>

using namespace std;

int N, M;
int board[50][50];
int visited[50][50];
int is_cycle = 0;

int dy[4] = {0, 1, 0, -1};
int dx[4] = {1, 0, -1, 0};

int dfs(pair<int, int> current) {
    int y = current.first;
    int x = current.second;
    if (y < 0 || x < 0 || y >= N || x >= M || is_cycle || board[y][x] == 0) return -1;

    // 아직 방문하지 않은 white 노드
    if (visited[y][x] == -1) {
        visited[y][x] = 0;
        for (int i=0; i<4; i++) {
            int cy = y + dy[i] * board[y][x];
            int cx = x + dx[i] * board[y][x];
            int r = dfs({cy, cx});
            if (visited[y][x] < r+1) visited[y][x] = r+1;
        }
        visited[y][x] = max(visited[y][x], 1);
        return visited[y][x];
    }
    // 현재 경로 상에 있는 grey 노드
    else if (visited[y][x] == 0) {
        is_cycle = 1;
        return 0;
    }
    // 이미 방문해서 dp에 저장된 black 노드
    else {
        return visited[y][x];
    }
}

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
    
    cin >> N >> M;

    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            char tmp;
            cin >> tmp;

            if (tmp == 'H') {
                board[i][j] = 0;
            } else {
                board[i][j] = tmp - '0';
            }
            visited[i][j] = -1;
        }
    }

    int answer = dfs({0, 0});

    // for (int i=0; i<N; i++) {
    //     for (int j=0; j<M; j++) {
    //         cout << visited[i][j] << " ";
    //     }
    //     cout << endl;
    // }

    if (is_cycle) {
        cout << -1 << endl;
    } else {
        cout << answer << endl;
    }
}