// 문제: https://www.acmicpc.net/problem/1002

#include <stdio.h>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);

    for (int i=0;i<t;i++) {
        int x1, y1, r1, x2, y2, r2;
        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);

        int d = pow(abs(x1 - x2), 2) + pow(abs(y1 - y2), 2);
        int gap = pow(abs(r1 - r2), 2);
        int summ = pow(r1 + r2, 2);

        if (gap < d && d < summ) {
            printf("2\n");
        } else if (gap == 0 && d == 0) {
            printf("-1\n");
        } else if (summ == d) {
            printf("1\n");
        } else if (gap == d) {
            printf("1\n");
        } else {
            printf("0\n");
        }

    }

    return 0;
}