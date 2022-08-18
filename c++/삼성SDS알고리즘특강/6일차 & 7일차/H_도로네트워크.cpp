// 문제 : https://www.acmicpc.net/problem/3176

#include <stdio.h>
#include <queue>
#include <vector>

using namespace std;

int N, M;
vector<pair<int, int>> lg[100001];
struct road {
    int p;
    int min=1000000;
    int max=0;
} parent[18][100001];

int depth[100001];

void LCS(int, int);

int main() {
    scanf("%d", &N);
    for (int i=0; i<N-1; i++) {
        int a, b, v;
        scanf("%d %d %d", &a, &b, &v);
        lg[a].push_back({b, v});
        lg[b].push_back({a, v});
    }
    // depth 초기화
    for (int i=0; i<=N; i++) depth[i] = -1;
    queue<int> q;
    q.push(1);
    depth[1] = 0;
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        for (pair<int, int> next : lg[cur]) {
            if (depth[next.first] == -1) {
                q.push(next.first);
                depth[next.first] = depth[cur] + 1;
                parent[0][next.first] = {cur, next.second, next.second};
            }
        }
    }
    
    // 점핑 테이블
    for (int r=1; r<18; r++) {
        for (int i=1; i<=N; i++) {
            road tmp = parent[r-1][parent[r-1][i].p];
            tmp.max = tmp.max < parent[r-1][i].max ? parent[r-1][i].max : tmp.max;
            tmp.min = tmp.min > parent[r-1][i].min ? parent[r-1][i].min : tmp.min;
            parent[r][i] = tmp;
        }
    }

    // for(int r=0; r<3; r++) {
    //     for (int i=1; i<=N; i++) {
    //         printf("%d %d %d | ", parent[r][i].p, parent[r][i].min, parent[r][i].max);
    //     }
    //     printf("\n");
    // }

    scanf("%d", &M);
    for (int i=0; i<M; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        LCS(a, b);
    }
}

void LCS(int a, int b) {
    // 1. Depth 맞추기
    if (depth[a] < depth[b]) {
        int tmp = a;
        a = b;
        b = tmp;
    }
    road tmpA = parent[0][a];
    road tmpB = parent[0][b];
    int diff = depth[a] - depth[b];
    for (int r=0; diff; r++) {
        if (diff & 1) {
            tmpA.max = tmpA.max > parent[r][a].max ? tmpA.max : parent[r][a].max;
            tmpA.min = tmpA.min > parent[r][a].min ? parent[r][a].min : tmpA.min;
            a = parent[r][a].p;
        }
        diff >>= 1;
    }
    int max = tmpA.max;
    int min = tmpA.min;

    // 2. 트리 올라가면서 찾기
    while (a != b) {
        int r;
        for (r=0; r<18; r++) {
            if (parent[r][a].p == parent[r][b].p) break;
        }
        if (r > 0) --r;
        tmpA.max = tmpA.max > parent[r][a].max ? tmpA.max : parent[r][a].max;
        tmpA.min = tmpA.min > parent[r][a].min ? parent[r][a].min : tmpA.min;
        a = parent[r][a].p;
        tmpB.max = tmpB.max > parent[r][b].max ? tmpB.max : parent[r][b].max;
        tmpB.min = tmpB.min > parent[r][b].min ? parent[r][b].min : tmpB.min;
        b = parent[r][b].p;

        max = tmpA.max > tmpB.max ? tmpA.max : tmpB.max;
        min = tmpA.min < tmpB.min ? tmpA.min : tmpB.min;
    }
    
    printf("%d %d\n", min, max);
}