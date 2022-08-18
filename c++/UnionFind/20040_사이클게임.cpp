// 문제 : https://www.acmicpc.net/problem/20040

#include <stdio.h>

using namespace std;

int N, M;
int parent[500000];

int find(int a) {
    if (parent[a] == a) return a;
    parent[a] = find(parent[a]);
    return parent[a];
}

void join(int a, int b) {
    int aRoot = find(a);
    int bRoot = find(b);
    parent[bRoot] = aRoot;
}

void sortedJoin(int a, int b) {
    int first = a < b ? a : b;
    int second = a > b ? a : b;
    join(first, second);
}

int main() {
    scanf("%d %d", &N, &M);
    for (int i=0; i<N; i++) parent[i] = i;
    
    int a, b;
    int count = 1;
    bool flag = true;
    for (int i=0; i<M; i++) {
        scanf("%d %d", &a, &b);
        if (find(a) == find(b)) {
            printf("%d\n", count);
            flag = false;
            break;
        }
        count++;
        sortedJoin(a, b);
    }
    if (flag) printf("0\n");
}