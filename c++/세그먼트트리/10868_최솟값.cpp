// 문제 : https://www.acmicpc.net/problem/10868

#include <stdio.h>
#include <string>

using namespace std;

int N, M, tmpN;
int tree[1024 * 512];

int min (int a, int b) { return a < b ? a : b; }

void make_tree() {
    for (int i=tmpN-1; i > 0; i--) {
        tree[i] = min(tree[i*2], tree[i*2+1]);
    }
}

int find_min(int a, int b) {
    int result = 1000000000;
    while (a <= b) {
        if (a % 2 == 1) result = min(result, tree[a]);
        if (b % 2 == 0) result = min(result, tree[b]);
        a = (a + 1) >> 1;
        b = (b - 1) >> 1;
    }
    return result;
}

int main() {
    scanf("%d %d", &N, &M);

    for (tmpN = 1; tmpN < N; tmpN = tmpN << 1);
    for (int i=0; i<=tmpN*2; i++) tree[i] = 1000000000;

    for (int i=tmpN; i<tmpN + N; i++) {
        scanf("%d", &tree[i]);
    }
    make_tree();

    int a, b;
    for (int i=0; i<M; i++) {
        scanf("%d %d", &a, &b);
        printf("%d\n", find_min(a+tmpN-1, b+tmpN-1));
    }
}