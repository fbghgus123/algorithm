// 문제: https://www.acmicpc.net/problem/1004

#include <stdio.h>
#include <vector>
#include <cmath>

using namespace std;

struct position {
    int x, y;
};

struct planet {
    position pos;
    int r;
};

int distance(position pos1, position pos2) {
    return pow(pos1.x - pos2.x, 2) + pow(pos1.y - pos2.y, 2);
}

bool isIn(position pos, planet p) {
    if (distance(pos, p.pos) < pow(p.r, 2)) {
        return true;
    }
    return false;
}

int check(position pos1, position pos2, planet p) {
    bool relationPos1 = isIn(pos1, p);
    bool relationPos2 = isIn(pos2, p);

    if ((relationPos1 && relationPos2) || (!relationPos1 && !relationPos2)) {
        return 0;
    }
    return 1;
}

int main() {
    int t;
    scanf("%d", &t);

    for (int i=0;i<t;i++) {
        int x1, y1, x2, y2;
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);

        position pos1 = { x1, y1 };
        position pos2 = { x2, y2 };

        int n;
        scanf("%d", &n);

        int answer = 0;

        for (int j=0;j<n;j++) {
            int x, y, r;
            scanf("%d %d %d", &x, &y, &r);
            planet p = { { x, y }, r };

            answer += check(pos1, pos2, p);
        }
        printf("%d\n", answer);
    }
}