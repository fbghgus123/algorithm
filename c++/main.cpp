#include <stdio.h>

using namespace std;

int N;
int tmpN;

int tree[1024 * 1024];

int find_upper(int a, int b) {
    a = tmpN + a;
    b = tmpN + b - 1;

    int acount = 1;
    int bcount = 1;

    int total = 0;
    while (a <= b) {
        if (a & 1 == 1) total += acount;
        if (a & 1 == 0) total += bcount;
        a = (a+1) >> 1;
        b = (b-1) >> 1;
        acount = acount >> 1;
        bcount = bcount >> 1;
    }
    return total;
}

int main() {
    scanf("%d", &N);
    for (tmpN=1; tmpN < N; tmpN = tmpN << 1);

    for (int i=0; i<tmpN*2; i++) tree[i] = 500000;
    for (int i=tmpN; i<tmpN + N; i++) {
        scanf("%d", &tree[i]);
    }
    for (int i=tmpN-1; i > 0; i--) {
        tree[i] = tree[i*2] > tree[i*2+1] ? tree[i*2] : tree[i*2+1];
    }

    for (int i=1; i<=N; i++) {
        printf("%d\n", find_upper(0, i));
    }
    return 0;
}