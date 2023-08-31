// 문제: https://www.acmicpc.net/problem/11758

#include <stdio.h>

using namespace std;

struct vec2 {
    int x, y;
};

int main() {
    int x1, y1, x2, y2, x3, y3;
    scanf("%d %d", &x1, &y1);
    scanf("%d %d", &x2, &y2);
    scanf("%d %d", &x3, &y3);

    vec2 u = {x2 - x1, y2 - y1};
    vec2 v = {x3 - x1, y3 - y1};

    int outerProductZ = u.x * v.y - u.y * v.x;
    if (outerProductZ > 0) {
        printf("1\n");
    } else if (outerProductZ < 0) {
        printf("-1\n");
    } else {
        printf("0\n");
    }
}