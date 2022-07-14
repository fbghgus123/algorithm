// 문제 : https://www.acmicpc.net/problem/1915

#include <stdio.h>

using namespace std;

int n, m;
int square[1000][1000];
int dp[1000][1000];

int maxx = 0;

int min(int a, int b, int c) {
    int minn = a < b ? a : b;
    minn = minn < c ? minn : c;
    return minn;
}

int main() {
    scanf("%d %d", &n, &m);
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            scanf("%1d", &square[i][j]);
            if (square[i][j] == 1) {
                dp[i][j] = 1;
                maxx = 1;
            }
        }
    }
    for (int i=1; i<n; i++) {
        for (int j=1; j<m; j++) {
            if (square[i][j] == 1 && square[i-1][j] == 1 && square[i][j-1] == 1 && square[i-1][j-1] == 1) {
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1;
                maxx = dp[i][j] > maxx ? dp[i][j] : maxx;
            }
        }
    }

    printf("%d\n", maxx * maxx);
}