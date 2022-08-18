// 문제 : https://www.acmicpc.net/problem/1717

#include <stdio.h>

using namespace std;

int N, M;
int parent[1000001];

int find(int a) {
    if (parent[a] == a) return a;
    else {
        parent[a] = find(parent[a]);
        return parent[a];
    }
}

void join(int a, int b) {
    int aRoot = find(a);
    int bRoot = find(b);
    parent[aRoot] = bRoot;
}

int main() {
    scanf("%d %d", &N, &M);
    for (int i=0; i<=1000000; i++) {
        parent[i] = i;
    }
    for (int i=0; i<M; i++) {
        int A, B, C;
        scanf("%d %d %d", &A, &B, &C);
        if (A == 1) {
            if (find(B) == find(C)) printf("YES\n");
            else printf("NO\n");
        } 
        else {
            join(B, C);
        }
    }
}