// 문제 : https://www.acmicpc.net/problem/2842

#include <stdio.h>
#include <queue>
#include <vector>

using namespace std;

int N, grid[50][50];
int minn = 1000000, maxx = 0;

struct p {
    int y, x;
};
p home;
vector<p> target;

int dy[8] = {0, 1, 0, -1, -1, -1, 1, 1};
int dx[8] = {1, 0, -1, 0, -1, 1, -1 ,1};

bool bfs(int a, int b) {
    if (a > grid[home.y][home.x] || b < grid[home.y][home.x]) return false;
    bool visited[50][50];
    for (int i=0; i<50; i++) for (int j=0; j<50; j++) visited[i][j] = true;
    queue<p> q;
    q.push(home);
    visited[home.y][home.x] = false;

    while (!q.empty()) {
        p current = q.front();
        q.pop();
        for (int i=0; i<8; i++) {
            int cy = current.y + dy[i];
            int cx = current.x + dx[i];
            if (0 <= cy && 0 <= cx && cy < N && cx < N) {
                if (visited[cy][cx] && a <= grid[cy][cx] && grid[cy][cx] <= b) {
                    visited[cy][cx] = false;
                    q.push({cy, cx});
                }
            }
        }
    }
    for (int i=0; i<target.size(); i++) {
        p current = target[i];
        if (visited[current.y][current.x]) return false;
    }
    return true;
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
    for (int i=0; i<N; i++) {
        char tmp[50];
        scanf("%s", tmp);
        for (int j=0; j<N; j++) {
            if (tmp[j] == 'P') home = {i, j};
            if (tmp[j] == 'K') target.push_back({i, j});
        }
    }
    for (int i=0; i<N; i++) for (int j=0; j<N; j++) {
        scanf("%d", &grid[i][j]);
        minn = minn > grid[i][j] ? grid[i][j] : minn;
        maxx = maxx < grid[i][j] ? grid[i][j] : maxx;
    }

    int answer = 1000000;
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