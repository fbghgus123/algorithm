// 문제 : https://www.acmicpc.net/problem/11050

#include <stdio.h>

#define ll long long

using namespace std;

int N, K;
ll memoization[100];

ll permutation(int num) {
    if (memoization[num] > 0) return memoization[num];
    memoization[num] = num * permutation(num-1);
    return memoization[num];
}

int main() {
    for (int i=0; i<11; i++) memoization[i] = 0;
    memoization[1] = 1;
    memoization[0] = 1;
    scanf("%d %d", &N, &K);
    if (K == 0) printf("1\n");
    else printf("%lld\n", permutation(N) / (permutation(N-K) * permutation(K)));
}