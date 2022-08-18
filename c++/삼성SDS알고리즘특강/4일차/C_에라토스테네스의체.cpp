// 문제 : https://www.acmicpc.net/problem/2960

#include <stdio.h>

using namespace std;

int N, K;
bool arr[1001];

int main() {
    scanf("%d %d", &N, &K);
    for (int i=0; i<=1000; i++) {
        arr[i] = true;
    }
    int count = 0;
    for (int i=2; i<=N; i++) {
        for (int j=1; i*j <= N; j++) {
            if (arr[i*j]) {
                count ++;
                arr[i*j] = false;
                if (count == K) {
                    printf("%d\n", i*j);
                }
            }
        }
    }
}