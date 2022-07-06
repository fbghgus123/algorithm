// 문제 : https://www.acmicpc.net/problem/2517

#include <stdio.h>
#include <algorithm>
#include <map>

using namespace std;

int N;
int tmpN;

int tree[1024 * 1024 * 2];
int nums[500000];
int order[500000];
map<int, int> mapp;

void update(int i) {
    tree[i]++;
    while (i > 0) {
        i = i >> 1;
        tree[i] = tree[i*2] + tree[i*2+1];
    }
}

int get_sum(int a, int b) {
    int sum = 0;
    while (a <= b) {
        if ((a&1) == 1) {
            sum += tree[a];
        }
        if ((b&1) == 0) {
            sum += tree[b];
        }
        a = (a+1) >> 1;
        b = (b-1) >> 1;
    }
    return sum;
}

int main() {
    scanf("%d", &N);
    for (tmpN = 1; tmpN < N; tmpN = tmpN << 1);
    for (int i=0; i < tmpN*2; i++) tree[i] = 0;
    
    for (int i=0; i<N; i++) scanf("%d", &order[i]);
    copy(order, order+N, nums);

    sort(nums, nums+N);
    for (int i=tmpN; i<tmpN+N; i++) {
        mapp.insert({nums[i-tmpN], i});
    }

    for (int i=0; i<N; i++) {
        int current = mapp[order[i]];
        update(current);
        printf("%d\n", i+1 - get_sum(tmpN, current-1));
    }

    return 0;
}