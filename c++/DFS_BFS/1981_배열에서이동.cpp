// 문제 : https://www.acmicpc.net/problem/1981

#include <stdio.h>
#include <queue>

using namespace std;

int N, grid[100][100], minn = 200, maxx = 0;

struct p {
    int y, x;
};

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

bool bfs(int a, int b) {
    if (a > grid[0][0] || a > grid[N-1][N-1] || b < grid[0][0] || b < grid[N-1][N-1]) return false;
    queue<p> q;
    bool visited[N][N];
    for (int i=0; i<N; i++) for (int j=0; j<N; j++) visited[i][j] = true; 
    visited[0][0] = false;
    q.push({0, 0});
    
    while (!q.empty()) {
        p current = q.front();
        q.pop();
        for (int i=0; i<4; i++) {
            int cy = current.y + dy[i];
            int cx = current.x + dx[i];
            if (0 <= cy && 0 <= cx && cy < N && cx < N) {
                if (grid[cy][cx] >= a && grid[cy][cx] <= b && visited[cy][cx]) {
                    if (cy == N-1 && cx == N-1) return true;
                    visited[cy][cx] = false;
                    q.push({cy, cx});
                }
            }
        }
    }
    return false;
}

int search_maxx(int left) {
    int answer = -1;
    int a = left;
    int b = maxx;
    int mid;
    while (a <= b) {
        mid = (a+b)/2;
        if (bfs(left, mid)) {
            answer = answer < mid && answer != -1 ? answer : mid;
            b = mid - 1;
        }
        else {
            a = mid + 1;
        }
    }
    return answer;
}

int search_minn(int right) {
    int answer = -1;
    int a = minn;
    int b = right;
    int mid;
    while (a <= b) {
        mid = (a+b)/2;
        if (bfs(mid, right)) {
            answer = answer > mid && answer != -1 ? answer : mid;
            a = mid + 1;
        }
        else {
            b = mid - 1;
        }
    }
    return answer;
}

int main() {
    scanf("%d", &N);
    for (int i=0; i<N; i++)
        for (int j=0; j<N; j++) {
            scanf("%d", &grid[i][j]);
            minn = grid[i][j] < minn ? grid[i][j] : minn;
            maxx = grid[i][j] > maxx ? grid[i][j] : maxx;
        }
    int answer = 200;
    while (minn <= maxx) {
        int tmpR = search_maxx(minn);
        if (tmpR == -1) break;
        int tmpL = search_minn(tmpR);
        if (tmpL == -1) break;
        answer = answer > tmpR - tmpL ? tmpR - tmpL : answer;
        minn = tmpL + 1;
    }
    printf("%d\n", answer);
}