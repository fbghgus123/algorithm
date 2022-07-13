// 문제 : https://www.acmicpc.net/problem/11404

#include <stdio.h>

using namespace std;

const int INF = 1e8;

int N, M;
int AM[101][101]; // 인접 행렬

int main() {
    scanf("%d %d", &N, &M);

    for (int i=1; i<=N; i++) {
        for (int j=1; j<=N; j++) {
            if (i != j) AM[i][j] = INF;
        }
    }

    int a, b, c;
    for (int i=1; i<=M; i++) {
        scanf("%d %d %d", &a, &b, &c);
        AM[a][b] = c < AM[a][b] ? c : AM[a][b]; // 유리한 간선 선택
    }

    for (int k=1; k<=N; k++) { // i: 출발지
        for (int i=1; i<=N; i++) { // j: 도착지
            for (int j=1; j<=N; j++) {
                if (AM[i][k] + AM[k][j] < AM[i][j]) {
                    AM[i][j] = AM[i][k] + AM[k][j];
                }
            }
        }
    }

    for (int i=1; i<=N; i++) {
        for (int j=1; j<=N; j++) {
            printf("%d ", AM[i][j] == INF ? 0 : AM[i][j]);
        }
        printf("\n");
    }
    return 0;
}