// 문제 : https://www.acmicpc.net/problem/7579

#include <stdio.h>
#include <algorithm>

using namespace std;

int N, M;

struct cost {
    int m, c;
} D[100];

bool cmp(cost a, cost b) {
    return a.c < b.c;
}

int sum() {
    int result = 0;
    for (int i=0; i<N; i++) {
        result += D[i].c;
    }
    return result;
}

int dp[101][10001];
int max (int a, int b) {
    return a > b ? a : b;
}

int main() {
    scanf("%d %d", &N, &M);
    for (int i=0; i<N; i++) {
        scanf("%d", &D[i].m);
    }
    for (int i=0; i<N; i++) {
        scanf("%d", &D[i].c);
    }

    sort(D, D+N, cmp);

    int total = sum();
    int time = total;
    for (int i=1; i<=N; i++) {
        for (int t=0; t<=total; t++) {
            if (t >= D[i-1].c) {
                dp[i][t] = max(dp[i-1][t], dp[i-1][t-D[i-1].c] + D[i-1].m);
                if (dp[i][t] >= M) {
                    time = time < t ? time : t;
                }
            }
            else {
                dp[i][t] = dp[i-1][t];
            }
        }
    }

    printf("%d\n", time);
}