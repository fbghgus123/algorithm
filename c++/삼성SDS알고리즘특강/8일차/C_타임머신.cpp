#include <stdio.h>
#include <climits>

int N, M;
struct e_t {
    int a, b, c;
} E[6001];

int visited[501];

int main() {
    scanf("%d %d", &N, &M);
    for (int i=1; i<=N; i++) visited[i] = INT_MAX;
    for (int i=1; i<= M; i++) {
        scanf("%d %d %d", &E[i].a, &E[i].b, &E[i].c);
    }

    // processing
    visited[1] = 0;
    bool isNegativeCycle = false;

    // N-1 만큼 돌리기
    for (int i=1; i<N; i++) {
        for (int j=1; j<=M; j++) {
            if (visited[E[j].a] < INT_MAX && visited[E[j].a] + E[j].c < visited[E[j].b]) {
                visited[E[j].b] = visited[E[j].a] + E[j].c;
            }
        }
    }

    // 음수 사이클 체크
    for (int j=1; j<=M; j++) {
        if (visited[E[j].a] < INT_MAX && visited[E[j].a] + E[j].c < visited[E[j].b]) {
            isNegativeCycle = true;
            break;
        }
    }

    if (isNegativeCycle) puts("-1");
    else {
        for (int i=2; i<=N; i++) {
            printf("%d\n", visited[i] == INT_MAX ? -1 : visited[i]);
        }
    }
    return 0;
}