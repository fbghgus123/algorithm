// 문제 : https://www.acmicpc.net/problem/7578

#include <stdio.h>

using namespace std;

int N, tmpN;
int A[500000], B[1000001];
int tree[1024 * 1024 * 2];

void update_tree(int a) {
    while (a > 0) {
        tree[a] += 1;
        a = a >> 1;
    }
}

int cnt_inverse(int a) {
    int sum = 0;
    a += tmpN;
    int b = tmpN + N - 1;
    while (a <= b) {
        if ((a&1) == 1) sum += tree[a];
        if ((b&1) == 0) sum += tree[b];
        a = (a+1) >> 1;
        b = (b-1) >> 1;
    }
    return sum;
}

int main() {
    scanf("%d", &N);
    for (tmpN=1; tmpN < N; tmpN = tmpN << 1);
    for (int i=0; i<=tmpN * 2; i++) tree[i] = 0;

    for (int i=0; i<N; i++) scanf("%d", &A[i]);
    for (int i=0; i<N; i++) {
        int val;
        scanf("%d", &val);
        B[val] = i;
    }
    
    long long int answer = 0;
    for (int i=0; i<N; i++) {
        int tmp = cnt_inverse(B[A[i]]);
        answer += tmp;
        update_tree(tmpN + B[A[i]]);
    }
    printf("%lld\n", answer);
}