// 문제 : https://www.acmicpc.net/problem/2579

#include <stdio.h>

using namespace std;

int n;
int stair[301];
int dp[301];

int max (int a, int b) {
    return a > b ? a : b;
}

int main() {
    scanf("%d", &n);
    for (int i=1; i<=n; i++) {
        scanf("%d", &stair[i]);
    }
    dp[1] = stair[1];
    if (n > 1) {
        dp[2] = stair[1] + stair[2];
        for (int i=3; i<=n; i++) {
            dp[i] = max(dp[i-3] + stair[i-1], dp[i-2]) + stair[i];
        }
    }
    printf("%d\n", dp[n]);
}