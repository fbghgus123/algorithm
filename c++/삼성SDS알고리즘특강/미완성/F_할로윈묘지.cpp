#include <stdio.h>
#include <cstring>
#include <queue>

using namespace std;

const int MAX = 1000000000;

int w, h, g, e;
int grid[30][30];
int dy[4] = {0, 1, 0, -1};
int dx[4] = {1, 0, -1, 0};

struct Node {
    int n, x1, y1, x2, y2, t;
} NS[902];

int P_size;
struct Path {
    int s, e, v;
} P[1024 * 1024];

int table[902];

void bfs(int n) {
    int visited[h][w];
    memset(visited, -1, sizeof(visited));
    queue<pair<int, int>> q;
    q.push({NS[n].y2, NS[n].x2});
    visited[NS[n].y2][NS[n].x2] = 0;
    while (!q.empty()) {
        pair<int, int> curr = q.front();
        q.pop();
        for (int i=0; i<4; i++) {
            int cy = curr.first + dy[i];
            int cx = curr.second + dx[i];
            if (0 <= cy && 0 <= cx && cy < h && cx < w) {
                if (visited[cy][cx] == -1 && grid[cy][cx] == 0) {
                    visited[cy][cx] = visited[curr.first][curr.second] + 1;
                    q.push({cy, cx});
                }
            }
        }
    }
    for (int i=1; i<=e+1; i++) {
        if (visited[NS[i].y1][NS[i].x1] == -1) continue;
        P[P_size++] = {n, i, visited[NS[i].y1][NS[i].x1] + NS[n].t};
    }
}

int main() {
    while (true) {
        scanf("%d %d", &w, &h);
        if (w == 0 && h == 0) break;

        memset(grid, 0, sizeof(grid));
        // 묘비 입력
        scanf("%d", &g);
        for (int i=0; i<g; i++) {
            int x, y;
            scanf("%d %d", &x, &y);
            grid[y][x] = 1;
        }
        // 시작 노드
        NS[0] = {0, 0, 0, 0, 0, 0};
        // 구멍 입력
        scanf("%d", &e);
        int x1, y1, x2, y2, t;
        for (int i=1; i<=e; i++) {
            NS[i].n = i;
            scanf("%d %d %d %d %d", &NS[i].x1, &NS[i].y1, &NS[i].x2, &NS[i].y2, &NS[i].t);
        }
        // 종료 노드
        NS[e+1] = {e+1, w-1, h-1, w-1, h-1, 0};

        // path 화
        P_size = 0;
        for (int i=0; i<=e; i++) {
            bfs(i);
        }

        // 테이블 초기화
        table[0] = 0;
        for (int i=1; i<=e+1; i++) table[i] = MAX;
        for (int i=0; i<e+1; i++) {
            for (int j=0; j<P_size; j++) {
                if (table[P[j].s] < MAX && table[P[j].e] > table[P[j].s] + P[j].v) {
                    table[P[j].e] = table[P[j].s] + P[j].v;
                }
            }
        }
        // 음수 사이클 확인
        bool NegativeCycle = false;
        for (int j=0; j<P_size; j++) {
            if (table[P[j].s] < MAX && table[P[j].e] > table[P[j].s] + P[j].v) {
                NegativeCycle = true;
                break;
            }
        }

        // 결과 출력
        if (NegativeCycle) printf("Never\n");
        else if (table[e+1] == MAX) printf("Impossible\n");
        else printf("%d\n", table[e+1]);
    }
}