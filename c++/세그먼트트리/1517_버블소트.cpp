// 문제 : https://www.acmicpc.net/problem/1517

#include <stdio.h>
#include <algorithm>
#include <map>

using namespace std;

int N, tmpN, A[500000], B[500000];
int tree[1024 * 512 * 2];
map<int ,int> mapping;

void update_tree(int a) {
    a += tmpN;
    while (a > 0) {
        tree[a] += 1;
        a = a >> 1;
    }
}

int get_cnt(int a) {
    int sum = 0;
    int b = tmpN + N;
    a += tmpN+1;
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
    for(tmpN = 1; tmpN < N; tmpN = tmpN << 1);
    for (int i=0; i<N; i++) {
        int tmp;
        scanf("%d", &tmp);
        A[i] = tmp;
        B[i] = tmp;
    }
    sort(B, B+N);
    for (int i=0; i<N; i++) {
        mapping.insert({B[i], i});
    }

    for (int i=0; i<tmpN*2; i++) tree[i] = 0;
    long long int answer = 0;
    for (int i=0; i<N; i++) {
        answer += get_cnt(mapping[A[i]]);
        update_tree(mapping[A[i]]);
    }
    printf("%lld\n", answer);
}