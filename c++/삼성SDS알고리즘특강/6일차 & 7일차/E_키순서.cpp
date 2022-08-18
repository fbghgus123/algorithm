// 문제 : https://www.acmicpc.net/problem/2458

#include <stdio.h>

using namespace std;

int N, M, a, b;
int distance[501][501];
const int INF = 1000000000;

int main() {
    scanf("%d %d", &N, &M);

    for (int i=1; i<=N; i++) {
        for (int j=1; j<=N; j++) {
            distance[i][j] = INF;
        }
    }

    for (int i=1; i<=M; i++) {
        scanf("%d %d", &a, &b);
        distance[a][b] = 1;
        distance[b][a] = -1;
    }

    for (int k=1; k<=N; k++) {
        for (int i=1; i<=N; i++) {
            for (int j=1; j<=N; j++) {
                if (distance[i][k] != INF && distance[i][k] == distance[k][j])
                    distance[i][j] = distance[i][k];
            }
        }
    }
    int answer = 0;
    for (int i=1; i<=N; i++) {
        for (int j=1; j<=N; j++) {
            if (i != j && distance[i][j] == INF) break;
            if (j == N) answer += 1;
        }
    }
    printf("%d\n", answer);
}