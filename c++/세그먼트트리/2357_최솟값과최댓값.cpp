// 문제 : https://www.acmicpc.net/problem/2357

#include <stdio.h>

using namespace std;

struct pair {
    int first, second;
};

int min(int a, int b) {
    return a < b ? a : b;
}

int max(int a, int b) {
    return a > b ? a : b;
}

int N, M;
pair tree[1024 * 512 * 2];
int tmpN;

void get_min_max(int a, int b) {
    int minn = 1000000000; int maxx = 0;
    while (a <= b) {
        if (a%2  == 1) {
            minn = tree[a].first != 0 && tree[a].first < minn ? tree[a].first : minn;
            maxx = tree[a].second > maxx ? tree[a].second : maxx;
        }
        if (b%2 == 0) {
            minn = tree[b].first != 0 && tree[b].first < minn ? tree[b].first : minn;
            maxx = tree[b].second > maxx ? tree[b].second : maxx;
        }
        a = (a+1) >> 1;
        b = (b-1) >> 1;
    }
    printf("%d %d\n", minn, maxx);
}

int main() {
    scanf("%d %d", &N, &M);

    for (tmpN = 1; tmpN<N; tmpN = tmpN << 1);
    for (int i=0; i<tmpN+N; i++) tree[i] = {0, 0};
    for (int i=tmpN; i<tmpN+N; i++) {
        int tmp;
        scanf("%d", &tmp);
        tree[i] = {tmp, tmp}; // 최소 최대
    }
    // 트리 초기화
    for (int i=tmpN-1; i>0; i--) {
        int minn, maxx;
        pair left = tree[i*2];
        pair right = tree[i*2+1];
        if (left.first == 0) minn = right.first;
        else if (right.first == 0) minn = left.first;
        else minn = min(left.first, right.first);
        maxx = max(left.second, right.second);
        tree[i] = {minn, maxx};
    }
    for (int i=0; i<M; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        get_min_max(tmpN+a-1, tmpN+b-1);
    }
}