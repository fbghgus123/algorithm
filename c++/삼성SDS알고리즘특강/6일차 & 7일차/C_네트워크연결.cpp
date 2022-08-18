// 문제 : https://www.acmicpc.net/problem/1922

#include <stdio.h>
#include <algorithm>

using namespace std;

int N, M;
int parent[1001];

struct e {
    int a, b, v;
    bool operator<(const e &ref) const {
        return this->v < ref.v;
    }
} edge[100000];

int find(int a) {
    if (parent[a] == a) return a;
    return find(parent[a]);
}

void join(int a, int b) {
    int rootA = find(a);
    int rootB = find(b);
    parent[rootB] = rootA;
}

int main() {
    scanf("%d", &N);
    for (int i=1; i<=N; i++) parent[i] = i;

    scanf("%d", &M);
    for (int i=0; i<M; i++) {
        scanf("%d %d %d", &edge[i].a, &edge[i].b, &edge[i].v);
    }

    int answer = 0, count = 0;
    sort(edge, edge+M);
    for (int i=0; i<M; i++) {
        if (find(edge[i].a) != find(edge[i].b)) {
            join(edge[i].a, edge[i].b);
            answer += edge[i].v;
            count++;
            if (count == N-1) break;
        }
    }
    printf("%d\n", answer);
    return 0;
}