// 문제 : https://www.acmicpc.net/problem/1256

#include <stdio.h>
#include <string>

using namespace std;

int N, M, K;
long long int  C[201][201];

int main() {
    scanf("%d %d %d", &N, &M, &K);
    C[0][0] = 1;
    for (int i=1; i<=N+M; i++) {
        C[i][0] = C[i][i] = 1;
        for (int j=1; j<i; j++) {
            long long int tmp = C[i-1][j] + C[i-1][j-1];
            if (tmp <= 10e9) C[i][j] = tmp;
            else C[i][j] = 10e9+1;
        }
    }
    if (C[N+M][N] < K) {
        printf("-1\n");
    }
    else {
        int tmp_sum = 0;
        string str = "";
        bool flag = false;
        while (N > 0 && M > 0) {
            if (tmp_sum > 10e9) {
                printf("-1\n");
                flag = true;
                break;
            }
            if (tmp_sum + C[N+M-1][N-1] < K) {
                tmp_sum += C[N+M-1][N-1];
                str += 'z';
                M--;
            } else {
                str += 'a';
                N--;
            }
        }
        if (!flag) {
            while (N>0) {
                str += 'a';
                N--;
            }
            while (M>0) {
                str += 'z';
                M--;
            }
            printf("%s\n", str.c_str());
        }
    }
}