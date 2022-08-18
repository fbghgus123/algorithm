// 문제 : https://www.acmicpc.net/problem/11049

#include <stdio.h>
#include <climits>

using namespace std;

int N;

int min(int a, int b) {
    return a < b ? a : b;
}

struct matrix {
    int r, c;
} M[500][500];

int dp[500][500];

int mull(int y1, int x1, int y2, int x2) {
    matrix a = M[y1][x1];
    matrix b = M[y2][x2];
    return a.r * a.c * b.c + dp[y1][x1] + dp[y2][x2];
}

int main() {
    scanf("%d", &N);
    for (int i=0; i<N; i++) {
        scanf("%d %d", &M[i][i].r, &M[i][i].c);
    }

    for (int i=1; i<N; i++) {
        for (int j=0; j<N-i; j++) {
            int minn = INT_MAX;
            M[j][j+i] = {M[j][j].r, M[j+i][j+i].c};
            for (int k=0; k<i; k++) {
                int tmp = mull(j, j+k, j+k+1, i+j);
                minn = tmp < minn ? tmp : minn;
            }
            dp[j][j+i] = minn;
        }
    }

    printf("%d\n", dp[0][N-1]);
}