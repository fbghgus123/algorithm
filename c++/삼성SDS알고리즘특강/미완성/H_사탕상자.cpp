#include <stdio.h>

using namespace std;

int N;
int tmpN;
int tree[1024 * 1024 * 2];

void update (int i, int v) {
    tree[i] += v;
    while (i > 0) {
        i = i >> 1;
        tree[i] = tree[i*2] + tree[i*2+1];
    }
}

int get_sum(int l, int r) {
    int sum = 0;
    while (l <= r) {
        if ((l&1) == 1) sum += tree[l];
        if ((r&1) == 0) sum += tree[r];
        l = (l+1) >> 1;
        r = (r-1) >> 1;
    }
    return sum;
}

int find_candy(int rank) {
    int l = 1;
    int r = 1000000;
    int mid;
    int answer;

    while (l <= r) {
        mid = (l+r)/2;

        int tmp = get_sum(tmpN + mid, tmpN + 1000000);
        printf("%d %d\n", mid, tmp);

        if (tmp >= rank) {
            l = mid + 1;
        }
        else {
            answer = mid;
            r = mid - 1;
        }
    }
    return answer;
}

int main() {
    scanf("%d", &N);
    for (tmpN = 1; tmpN < 100000; tmpN = tmpN << 1);
    for (int i=0; i<tmpN*2; i++) tree[i] = 0;

    for (int i=0; i<N; i++) {
        int a, b, c;
        scanf("%d", &a);
        if (a == 1) {
            scanf("%d", &b);
            printf("%d\n", find_candy(b));
        } else {
            scanf("%d %d", &b, &c);
            update(b+tmpN-1, c);
        }
    }

    printf("%d\n", tree[1000000]);
}