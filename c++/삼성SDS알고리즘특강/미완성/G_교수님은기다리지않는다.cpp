#include <stdio.h>
#include <vector>

using namespace std;

int N, M;
pair<int, long long int> parent[100001];

pair<int, long long int> find(int a) {
    if (parent[a].first == a) return parent[a];
    else {
        pair<int, long long int> tmp = find(parent[a].first);
        parent[a] = {tmp.first, tmp.second + parent[a].second};
        return parent[a];
    }
}

void join(int a, int b, int c) {
    pair<int, long long int> aRoot = find(a);
    pair<int, long long int> bRoot = find(b);
    pair<int, long long int> tmp = {bRoot.first, c - parent[a].second};
    parent[aRoot.first] = tmp;
}

int main() {
    while (1) {
        scanf("%d %d", &N, &M);
        if (N == 0 && M == 0) break;

        // 이니셜라이즈
        for (int i=1; i<=N; i++) parent[i] = {i, 0};
        for (int i=0; i<M; i++) {
            char cmd;
            int A, B, C;
            scanf("%c", &cmd);
            if (cmd == '!') {
                scanf("%d %d %d", &A, &B, &C);
                join(A, B, C);
            }
            else {
                scanf("%d %d", &A, &B);
                pair<int, long long int> tmpA = find(A);
                pair<int, long long int> tmpB = find(B);
                if (tmpA.first == tmpB.first) {
                    printf("%lld\n", tmpB.second - tmpA.second);
                }
                else {
                    printf("UNKNOWN\n");
                }
            }
        }
    }
    return 0;
}