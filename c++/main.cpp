#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>

#define MAX 100

using namespace std;

int T;
char grid[MAX][MAX];

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int bfs(pair<int, int> S, int N, int M, int K) {
    int visited[N][M];
    int result = 0;
    memset(visited, 0, sizeof(visited));
    visited[S.first][S.second] = 1;

    queue<pair<int, int>> q;
    q.push(S);
    
    while (q.size() != 0) {
        pair<int, int> current = q.front();
        q.pop();
        for (int i=0; i<4; i++) {
            int cy = current.first + dy[i];
            int cx = current.second + dx[i];
            if (0 <= cy && 0 <= cx && cy < N && cx < M) {
                if (visited[cy][cx] == 0 && grid[cy][cx] != 'X' && visited[current.first][current.second] < K) {
                    q.push({cy, cx});
                    visited[cy][cx] = visited[current.first][current.second] + 1;
                }
            } else {
                result = (result + 1) % 1000000007;
            }
        }
    }

    for(int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cout << visited[i][j] << " ";
        }
        cout << endl;
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> T;
    for(int t=1; t<=T; t++) {
        int N, M, K;
        cin >> N >> M >> K;
        pair<int, int> S;
        for (int i=0; i<N; i++) {
            for (int j=0; j< M; j++) {
                cin >> grid[i][j];
                if (grid[i][j] == 'S') S = {i, j};
            }
        }
        
        cout << "#" << t << " " << bfs(S, N, M, K) << endl;;
    }
}