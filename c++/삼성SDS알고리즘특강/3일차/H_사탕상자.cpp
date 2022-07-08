// 문제 : https://www.acmicpc.net/problem/2243

#include <stdio.h>

#define MAX 1000000

using namespace std;

int tree[1024 * 1024 * 2];
int N, tmpN;

void update_tree(int n, int amount) {
    while (n > 0) {
        tree[n] += amount;
        n = n >> 1;
    }
}

int get_sum(int a, int b) {
    int sum = 0;
    while (a <= b) {
        if ((a&1) == 1) sum += tree[a];
        if ((b&1) == 0) sum += tree[b];
        a = (a+1) >> 1;
        b = (b-1) >> 1;
    }
    return sum;
}

// 순위를 포함하는 것 중 제일 작은 맛 반환 + 사탕 하나 빼기
int get_candy(int rank) {
    int left = 1;
    int right = MAX;
    int mid, answer;

    while (left <= right) {
        mid = (left + right) / 2;
        if (get_sum(tmpN, tmpN + mid) >= rank) {
            answer = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    update_tree(tmpN + answer, -1);
    return answer;
}

int main() {
    for (tmpN = 1; tmpN < MAX; tmpN = tmpN << 1);
    for (int i=tmpN; i < tmpN + MAX; i++) tree[i] = 0;

    scanf("%d", &N);
    for (int i=0; i<N; i++) {
        int a, b, c;
        scanf("%d", &a);

        // 맛 출력
        if (a == 1) {
            scanf("%d", &b);
            printf("%d\n", get_candy(b));
        }
        // tree 업데이트
        else {
            scanf("%d %d", &b, &c);
            update_tree(tmpN + b, c);
        }
    }
}