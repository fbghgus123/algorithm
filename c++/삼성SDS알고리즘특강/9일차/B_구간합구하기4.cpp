// 문제 : https://www.acmicpc.net/problem/11659

#include <stdio.h>

using namespace std;

int N, M;
int num[100000];
int add[100000];

int main() {
    scanf("%d %d", &N, &M);
    for (int i=0; i<N; i++) {
        scanf("%d", &num[i]);
    }
    add[1] = num[0];
    for (int i=2; i<=N; i++) {
        add[i] = add[i-1] + num[i-1];
    }

    int a, b;
    for (int i=0; i<M; i++) {
        scanf("%d %d", &a, &b);
        printf("%d\n", add[b] - add[a-1]);
    }
}