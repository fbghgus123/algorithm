// 문제 : https://www.acmicpc.net/problem/2887

#include <stdio.h>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

int N, parent[100000];

int abs(int a) {
    return a < 0 ? -a : a;
}

int min(int a, int b) {
    return a < b ? a : b;
}

struct position {
    int n;
    int x, y, z;
} P[100000];

bool cmpX (position a, position b) {
    return a.x < b.x;
}

bool cmpY (position a, position b) {
    return a.y < b.y;
}

bool cmpZ (position a, position b) {
    return a.z < b.z;
}

int find(int a) {
    if (a == parent[a]) return a;
    parent[a] = find(parent[a]);
    return parent[a];
}

void join(int a, int b) {
    int aRoot = find(a);
    int bRoot = find(b);
    parent[bRoot] = aRoot;
}

int main() {
    scanf("%d", &N);
    for (int i=0; i<N; i++) {
        parent[i] = i;
        P[i].n = i;   
        scanf("%d %d %d", &P[i].x, &P[i].y, &P[i].z);
    }

    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int,int> >>> pq;

    sort(P, P+N, cmpX);
    for (int i=1; i<N; i++) {
        pq.push({abs(P[i].x - P[i-1].x), {P[i].n, P[i-1].n}});
    }

    sort(P, P+N, cmpY);
    for (int i=1; i<N; i++) {
        pq.push({abs(P[i].y - P[i-1].y), {P[i].n, P[i-1].n}});
    }

    sort(P, P+N, cmpZ);
    for (int i=1; i<N; i++) {
        pq.push({abs(P[i].z - P[i-1].z), {P[i].n, P[i-1].n}});
    }

    int count = 0;
    int answer = 0;
    while (count < N-1) {
        pair<int, pair<int, int> > tmp = pq.top();
        pq.pop();

        int a = tmp.second.first;
        int b = tmp.second.second;
        if (find(a) != find(b)) {
            count++;
            join(a, b);
            answer += tmp.first;
        }
    }
    printf("%d\n", answer);
}