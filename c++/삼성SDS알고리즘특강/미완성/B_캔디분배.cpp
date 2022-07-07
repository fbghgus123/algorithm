#include <stdio.h>

using namespace std;

int k, c;

int gcd(int a, int b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a%b);
}

int abs(int num) {
    return num < 0 ? -num : num;
}

int get_candy(int A, int B, int C, int D) {
    int first = c*A + k*B;
    int second = c*C + k*D;
    int mod = first % second;
    int quantity = first / second;

    // printf("%d %d %d\n%d %d %d\n\n", A, B, first, C, D, second);

    int tmpC = A - C * quantity;
    int tmpD = B - D * quantity;

    if (mod == 1) {
        if (tmpC > 0) {
            return tmpC;
        } else {
            return C - tmpC;
        }
    } else {
        return get_candy(C, D, tmpC, tmpD);
    }
}

int main() {
    int t;
    scanf("%d", &t);

    for (int i=0; i<t; i++) {
        scanf("%d %d", &k, &c);
        if (k+1 < c || gcd(k, c) != 1 || k == 1000000000) {
            printf("IMPOSSIBLE\n");
        }
        else if (c == 1) {
            printf("%d\n", k+1);
        }
        else {
            int ans =  get_candy(0, 1, 1, 0);
            if (ans > 1000000000) {
                printf("IMPOSSIBLE\n");
            } else {
                printf("%d\n", get_candy(0, 1, 1, 0));
            }
        }
    }
}