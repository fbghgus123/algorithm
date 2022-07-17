// 문제 : https://www.acmicpc.net/problem/1976

#include <stdio.h>

using namespace std;

int N, M;
int parent[201];
int grid[201][201];
int prev = 0;

int find(int a) {
    if (a == parent[a]) return a;
    parent[a] = find(parent[a]);
    return parent[a];
}

void join(int a, int b) {
    int aRoot = find(a);
    int bRoot = find(b);
    parent[aRoot] = bRoot;
}

int main () {
    scanf("%d %d", &N, &M);
    for (int i=1; i<=N; i++) parent[i] = i;
    for (int i=1; i<=N; i++) {
        for (int j=1; j<=N; j++) {
            scanf("%d", &grid[i][j]);
        }
    }

    for (int i=1; i<N; i++) {
        for (int j=i+1; j<=N; j++) {
            if (grid[i][j] == 1) join(i, j);
        }
    }

    bool flag = true;
    for (int i=0; i<M; i++) {
        int tmp;
        scanf("%d", &tmp);
        if (prev == 0) prev = find(tmp);
        else {
            if (prev != find(tmp)) flag = false;
        }
    }
    if (flag) printf("YES\n");
    else printf("NO\n");
}