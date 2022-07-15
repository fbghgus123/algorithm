// 문제 : https://www.acmicpc.net/problem/2098
#include <stdio.h>
#include <queue>

const int SIZE = (1 << 16);
int ALLVISITED;

using namespace std;

int N;
int w[16][16];
int dp[16][SIZE];

int min (int a, int b) {return a < b ? a : b;}

int dfs(int curr, int visited) {
    if (!dp[curr][visited]) {
        if (visited == ALLVISITED) {
            dp[curr][visited] = w[0][curr];
        }
        else {
            dp[curr][visited] = 20000000;
            for (int next=1; next<N; next++) {
                // 경로중 이미 방문한 곳이라면 패스
                if (visited & (1 << next)) continue;
                dp[curr][visited] = min(dp[curr][visited], dfs(next, visited | 1 << next) + w[next][curr]);
            }
        }
    }
    return dp[curr][visited];
}

int main() {
    scanf("%d", &N);
    ALLVISITED = (1 << N) - 1;

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            scanf("%d", &w[i][j]);
            if (!w[i][j]) w[i][j] = 20000000;
        }
    }
    printf("%d\n", dfs(0, 1));
}