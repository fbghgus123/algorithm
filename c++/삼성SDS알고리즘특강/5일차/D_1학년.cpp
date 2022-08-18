// 문제 : https://www.acmicpc.net/problem/5557

#include <stdio.h>

using namespace std;

int N, answer;
int nums[100];
long long int dp[101][21];

void btk(int index) {
    for (int i=0; i<21; i++) {
        if (dp[index][i] > 0) {
            if (nums[index+1] + i <= 20) dp[index+1][nums[index+1]+i] += dp[index][i];
            if (i - nums[index+1] >= 0) dp[index+1][i-nums[index+1]] += dp[index][i];
        }
    }
}

int main() {
    scanf("%d", &N);
    for (int i=0; i<N-1;i++) {
        int num;
        scanf("%d", &num);
        nums[i] = num;
    }
    scanf("%d", &answer);

    for (int i=0; i<101; i++) {
        for (int j=0; j<21; j++) {
            dp[i][j] = 0;
        }
    }

    dp[0][nums[0]] = 1;
    for (int i=0; i<N-2; i++)
        btk(i);
    
    // for (int i=0; i<N; i++) {
    //     for (int j=0; j<21; j++) {
    //         printf("%d ", dp[i][j]);
    //     }
    //     printf("\n");
    // }

    printf("%lld\n", dp[N-2][answer]);
}