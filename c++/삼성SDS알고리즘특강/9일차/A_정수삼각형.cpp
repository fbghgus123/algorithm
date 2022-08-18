// 문제 : https://www.acmicpc.net/problem/1932

#include <stdio.h>

using namespace std;

int n;
int score[501][501];
int dp[501][501];

int maxx = 0;

int max(int a, int b) {
    return a > b ? a : b;
}

int main() {
    scanf("%d", &n);
    for (int i=0; i<n; i++) {
        for (int j=0; j<=i; j++) {
            scanf("%d", &score[i][j]);
        }
    }

    dp[0][0] = score[0][0];
    maxx = score[0][0];
    for (int i=1; i<n; i++) {
        for (int j=0; j<=i; j++) {
            if (j == 0) {
                dp[i][j] = dp[i-1][j] + score[i][j];
            }
            else if (j == i) {
                dp[i][j] = dp[i-1][j-1] + score[i][j];
            }
            else {
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + score[i][j];
            }
            maxx = max(dp[i][j], maxx);
        }
    }
    printf("%d\n", maxx);
}